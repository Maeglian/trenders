import os

from flask import Flask

from trends.clients.google import start_get_trends
from trends.clients.prefs import cache
from trends.handlers.trends import trends



def create_app(db_url):
    app = Flask(__name__)
    # app.db = create_engine(db_url) #do we need db at all here?
    app.register_blueprint(trends, url_prefix='/')
    cache.init_app(app)
    start_get_trends()
    return app


