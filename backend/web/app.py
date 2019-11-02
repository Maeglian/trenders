import os

from trends.app import create_app

if __name__ == '__main__':
    # export DATABASE_URL=postgresql://me:hackme@0.0.0.0/trends
    # run db
    # docker run  --rm -e POSTGRES_DB=trends -e POSTGRES_USER=me -e POSTGRES_PASSWORD=hackme -p 5432:5432 postgres:10.7
    print('DATABASE_URL', os.environ['DATABASE_URL'])

    app = create_app(os.environ['DATABASE_URL'])
    app.run(host='0.0.0.0', port=8080)
