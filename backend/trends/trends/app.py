from flask import Flask
from trends.db import create_engine
from trends.handlers.trends import trends


def create_app(db_url):
    app = Flask(__name__)
    app.db = create_engine(db_url)
    app.register_blueprint(trends, url_prefix='/')
    return app
