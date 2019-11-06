from flask import Blueprint, Response
from trends.clients.google import get_trends_cached

trends = Blueprint('trends', __name__)

@trends.route('/fetch', methods=['GET'])
def import_trends():
    json = get_trends_cached()
    if json is not None:
        return Response(response=json, status=200)
    else:
        return Response(response="Cache is empty", status=400)
