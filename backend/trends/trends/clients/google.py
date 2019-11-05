import json
import logging
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from trends.clients.prefs import RealTrendReq, cache


global_dict = {"fired": 0}


def get_trends():
    logging.basicConfig()
    logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    trend_getter = RealTrendReq()
    today_searches_df = trend_getter.today_searches_fine(pn='RU')
    # global_dict['fired'] = global_dict.get("fired") + 1
    # today_searches_df = global_dict
    response = json.dumps(
        {'data': today_searches_df},
        ensure_ascii=False)

    cache.set('trends', response)
    print(response)
    return response


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
    return cache.get('trends')
