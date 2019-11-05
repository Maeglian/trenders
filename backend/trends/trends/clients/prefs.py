from flask_caching import Cache
from pytrends.request import TrendReq



class RealTrendReq(TrendReq):
    def today_searches_fine(self, pn='RU'):
        """Requests data from Google Daily Trends section for daily trends
        Returns (date, trend) pairs only for current date"""
        trends_list = list()
        keys = ('title', 'avatar', 'description')
        forms = {'ns': 15, 'geo': pn, 'tz': '-180', 'hl': 'en-US'}
        req_json = self._get_data(
            url=TrendReq.TODAY_SEARCHES_URL,
            method=TrendReq.GET_METHOD,
            trim_chars=5,
            params=forms
        )['default']['trendingSearchesDays'][0]
        date = req_json['date']
        trends = req_json['trendingSearches']
        for trend in trends:
            title = (trend['title']['query']).replace(u'\xa0', u' ')
            avatar = trend['image']['imageUrl']
            description = (trend['articles'][0]['title']).replace(u'&quot;', u' ')
            record = (title, avatar, description)
            trends_list.append(dict(zip(keys, record)))
        return trends_list


cache = Cache(config={'CACHE_TYPE': 'simple', "CACHE_DEFAULT_TIMEOUT": 0})
