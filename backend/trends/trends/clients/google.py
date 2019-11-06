import json
import logging
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from trends.clients.prefs import RealTrendReq, cache


def get_trends():
    """
    Gets trends from google-trend, makes json, an put then to cache
    """
    # TODO: resolve problems with logging from another thread
    logging.basicConfig()
    logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    trend_getter = RealTrendReq()
    try:
        today_searches_df = trend_getter.today_searches_fine(pn='RU')
        response = json.dumps(
            {'data': today_searches_df},
            ensure_ascii=False)
        logging.debug("Got trends %s", response)
        cache.set('trends', response)
    except Exception as e:
        logging.error("Can't get trends from google due to %s", e)
        raise


def start_get_trends():
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(get_trends,
                            trigger='interval',
                            next_run_time=datetime.now(),
                            minutes=15,
                            jitter=120
                            )
    scheduler.start()


def get_trends_cached():
    """
        get treads json from cache
        returns None if there are no key 'trends' in cache
    """
    return cache.get('trends')
