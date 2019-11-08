import os
from flask import Flask
from content.db import create_engine
from content.handlers.content import content


def create_app(db_url):
    app = Flask(__name__)
    # app.db = create_engine(db_url)
    app.register_blueprint(content, url_prefix='/')
    return app


if __name__ == '__main__':
    # export DATABASE_URL=postgresql://me:hackme@0.0.0.0/content
    # run db
    # docker run  --rm -e POSTGRES_DB=content -e POSTGRES_USER=me -e POSTGRES_PASSWORD=hackme -p 5432:5432 postgres:10.7
    # print('DATABASE_URL', os.environ['DATABASE_URL'])

    app = create_app(None)  # os.environ['DATABASE_URL']
    app.run(host='0.0.0.0', port=8080)
