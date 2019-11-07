import json
import logging
import logging.config

from flask import Blueprint, Response
from flask import request

from content.utils.feed_request import FeedRequest


content = Blueprint('content', __name__)
# logging.config.fileConfig('logging.conf')
# log = logging.getLogger()


@content.route('/api/feed', methods=['GET'],)
def feed_proxy():
    limit = request.args.get('limit')
    tag = request.args.get('tag')
    offset = request.args.get('offset')

    # log.info('GET /api/feed?tag=%s&offset=%s&limit=%s', tag, offset, limit)
    fr = FeedRequest()
    resp = fr.get_response(tag=tag, offset=offset, limit=limit)
    return Response(
        json.dumps({"data": resp.json()}, ensure_ascii=False),
        status=resp.status_code, mimetype='application/json'
    )
