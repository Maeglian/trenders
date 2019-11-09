from flask import Blueprint, Response
from comment_trends.trends_logic.trends import get_trends_cached, tags

comment_trends = Blueprint('trends', __name__)


@comment_trends.route('/fetch/<tag>', methods=['GET'])
def import_trends(tag):
    if tag not in tags:
        return Response(response="Tag absent in tag list", status=400)

    json = get_trends_cached(tag)
    if json is not None:
        return Response(response=json, status=200)
    else:
        return Response(response="Cache is empty", status=400)
