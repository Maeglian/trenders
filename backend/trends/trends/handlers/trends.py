from flask import Blueprint, Response
from trends.clients.google import get_trends_cached
from trends.clients.prefs import cache

trends = Blueprint('trends', __name__)


@trends.route('/fetch', methods=['GET'])
def import_trends():
    """
    Get json with google trends from cache and returns it
    :return: flask. Response with google trends as json,
    if cache is empty returns 400 status
    """
    json = get_trends_cached(cache)
    if json is not None:
        return Response(response=json, status=200)
    else:
        return Response(response="Cache is empty", status=400)
