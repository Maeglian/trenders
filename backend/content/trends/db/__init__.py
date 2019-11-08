import sqlalchemy as sa


def create_engine(db_url):
    engine = sa.create_engine(
        db_url,
        # echo=True   # useful for debugging
    )
    return engine
