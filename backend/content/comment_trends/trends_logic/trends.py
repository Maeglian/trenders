from collections import defaultdict, namedtuple
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
from pprint import pprint
import json

from flask_caching import Cache

from comment_trends.external_api.feed import FeedRequest
from comment_trends.external_api.player import PlayerRequest
from comment_trends.external_api.comments import CommentsRequest

Counts = namedtuple('Counts', ['day', 'week', 'month'])
cache = Cache(config={'CACHE_TYPE': 'simple', "CACHE_DEFAULT_TIMEOUT": 0})
config = {'offset': 0, 'limit': 2, 'num_docs': 4}
tags = {"movie", "series", "kids", "sport", "blogger"}


def get_trends_cached(tag):
    return cache.get(tag)


def compute_trends():
    for tag in tags:
        result = get_sorted_trends(tag)
        cache.set(tag, json.dumps(result, ensure_ascii=False))


def get_sorted_trends(tag):
    themes = get_potential_trends(tag, config)
    sorted_themes = sorted(themes.items(), key=lambda x: x[1].day, reverse=True)
    result = []
    for (theme_id, theme_title), _ in sorted_themes:
        result.append({
            'id': theme_id,
            'title': theme_title
        })

    return {'data': result}


def get_potential_trends(tag, feed_params, step=1) -> Dict[Tuple[str, str], Counts]:

    limit = feed_params['limit']
    documents = dict()

    for i in range(0, limit, step):
        feed_params['offset'] = i
        feed_params['limit'] = i + step if i + step <= limit else limit
        documents.update(get_documents(tag, feed_params))

    doc_to_comments = get_comments(documents)
    theme_to_comments = group_comments_by_themes(documents, doc_to_comments)
    theme_to_count = count_comments_by_themes(theme_to_comments)

    return theme_to_count


def get_documents(tag, feed_params) -> Dict[str, dict]:
    feed_request = FeedRequest()
    response = feed_request.get_response(tag=tag, **feed_params)
    return response.get_documents()


def get_comments(documents):
    doc_to_comments = dict()
    for doc_id in documents:
        response = CommentsRequest.get_response(doc_id)
        doc_to_comments[doc_id] = response.get_timestamps()
    return doc_to_comments


def group_comments_by_themes(documents, doc_to_comments) -> Dict[Tuple[str, str], List]:
    themes_to_comments = defaultdict(list)

    for doc_id in documents:
        response = PlayerRequest.get_response(doc_id)
        themes = response.get_themes()

        for theme in themes:
            themes_to_comments[(theme['id'], theme['title'])].extend(doc_to_comments[doc_id])

    return themes_to_comments


def count_comments_by_themes(theme_to_comments):
    theme_to_count = dict()

    for theme_id in theme_to_comments:
        # theme_id ~ (theme_id, theme_title)
        theme_to_comments[theme_id] = [int((str(ts)[:-6])) for ts in theme_to_comments[theme_id]]
        theme_to_count[theme_id] = count_comments(theme_to_comments[theme_id])

    return theme_to_count


def count_comments(comments):
    comments.sort(reverse=True)
    today = datetime.today()
    day = count_comments_from(comments, today - timedelta(days=1))
    week = count_comments_from(comments, today - timedelta(days=7))
    month = count_comments_from(comments, today - timedelta(days=30))

    return Counts(day=day, week=week, month=month)


def count_comments_from(comment_ts, start):
    start = start.timestamp()
    count = 0
    for timestamp in comment_ts:
        if timestamp > start:
            count += 1
        else:
            break

    return count


if __name__ == '__main__':
    pprint(get_sorted_trends('movie'))

