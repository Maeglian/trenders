import logging
import requests

from trends.collectors.base import BaseCollector

REQUEST_INTERVAL = 1
REQUEST_JITTER = 1


class EfirCollector(BaseCollector):
    def __init__(self, repo, url):
        super().__init__(repo, "efir", REQUEST_INTERVAL, REQUEST_JITTER)
        self.source_link = url

    def collect(self):
        logging.info("efir collect")
        try:
            response = requests.get(self.source_link)
            print("efir collect response {0}".format(response.content))
            return self.insert(response.content)
        except Exception as e:
            logging.error("failed to collect efir {0}".format(str(e)))

