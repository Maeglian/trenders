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


if __name__ == '__main__':
    # export DATABASE_URL=postgresql://me:hackme@0.0.0.0/trends
    # run db
    # docker run  --rm -e POSTGRES_DB=trends -e POSTGRES_USER=me -e POSTGRES_PASSWORD=hackme -p 5432:5432 postgres:10.7
    # print('DATABASE_URL', os.environ['DATABASE_URL'])

    app = create_app(None) # os.environ['DATABASE_URL'])
    app.run(host='0.0.0.0', port=8080)