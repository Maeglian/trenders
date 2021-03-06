import json

from trends.models.trends import content_table, trend_table
from sqlalchemy import desc
import logging
from sqlalchemy.sql import select

from datetime import datetime, timedelta


class Repository:

    def __init__(self, db):
        self.db = db

    @staticmethod
    def get_utc_date(date):  # sort of
        return date - date.tzinfo.utcoffset(date)

    @staticmethod
    def is_current_day(date):
        now = datetime.utcnow()
        date -= date.tzinfo.utcoffset(date)
        return not (now.day - date.day)

    def insert_trend(self, trend_json):
        with self.db.begin() as conn:
            with conn.begin():
                data = {
                    "data": json.loads(trend_json)['data'],
                }
                s = select([trend_table.c.id, trend_table.c.created_at]). \
                    order_by(trend_table.c.id.desc()).limit(1)
                last_entry = conn.execute(s).fetchone()
                date = self.get_utc_date(last_entry['created_at'])
                if self.is_current_day(date):
                    logging.getLogger(__name__).\
                        debug("About to change entry for current day for the new one")
                    id_to_delete = last_entry['id']
                    delete_stmt = trend_table.delete(). \
                        where(trend_table.c.id == id_to_delete)
                    result = conn.execute(delete_stmt)
                    logging.getLogger(__name__).\
                        debug("%s entry were deleted", result.rowcount)
                conn.execute(trend_table.insert(), **data)

    def insert_content(self, content_json):
        with self.db.begin() as conn:
            with conn.begin():
                # print("repo insert content", json.loads(content_json))
                data = [
                    {"category": key, "data": value}
                    for key, value in json.loads(content_json).items()
                ]
                conn.execute(content_table.insert(), *data)

    def read_all(self, limit, period):
        pass

    def trend_record_row_to_dict(self, trend_rec):
        """
        Returns:

        [
        {
            "day": 1,
            "data": {
                ...
            }
        },
        {
            "day": 22,
            "data": {
                ...
            }
        }
        ]"""

        result = []

        for trend in trend_rec[0]:
            d = dict(trend)

            # Надо ли мапить поля? Если каких то нет, то не добавлять этот тренд?

            # d['id'] = d['id']
            # d['title'] = d['title'].value
            # d['avatar'] = d['avatar'].value
            # d['description'] = d['description'].value
            # d['bg'] = d['bg'].value

            result.append({
                "day": d["day"],
                "data": d}
            )
        return result

    def read_trend(self, period):
        with self.db.begin() as conn:
            with conn.begin():
                p = datetime.today() - timedelta(days=period)
                s = select([trend_table.c.data]). \
                    where(trend_table.c.created_at >= p). \
                    order_by(desc(trend_table.c.created_at))

                rows = conn.execute(s)

                result = []
                # Выбираем все, что вернули: строка - один день
                for trend in rows:
                    result += self.trend_record_row_to_dict(trend)

                logging.getLogger(__name__).info("google trends num rows: {0}".format(len(result)))
                return result

    def read_content(self, period, tag):
        with self.db.begin() as conn:
            with conn.begin():
                p = datetime.today() - timedelta(days=period)
                s = select([content_table.c.data]). \
                    where(content_table.c.created_at >= p). \
                    where(content_table.c.category == tag). \
                    order_by(desc(content_table.c.created_at))

                rows = conn.execute(s)

                result = []
                # Выбираем все, что вернули: строка - один день
                for trend in rows:
                    result += self.trend_record_row_to_dict(trend)

                logging.getLogger(__name__).info("efir trends num rows: {0}".format(len(result)))
                return result
