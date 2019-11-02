from flask import Blueprint, Response

trends = Blueprint('trends', __name__)


@trends.route('/', methods=['GET'])
def import_trends():
    return Response('Hi!', status=200)
