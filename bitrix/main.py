import datetime
import json

import os
import requests

from django.conf import settings


class Bitrix24:
    webhook_url = getattr(settings, 'BITRIX_WEBHOOK_URL', '')
    log_file_path = getattr(settings, 'BITRIX_LOG_FILE', 'bitrix_log')
    auto_log = True

    def build_url(self, method):
        return self.webhook_url + str(method)

    def build_log_file_path(self):
        if os.path.isdir(self.log_file_path):
            return self.log_file_path + '/bitrix_log.txt'
        return self.log_file_path

    def send_request(self, url, params):
        response = requests.post(url, json=params)
        if self.auto_log:
            self._log(response)
        try:
            return response.json()
        except:
            return response.status_code

    def call_method(self, method, params):
        url = self.build_url(method)
        return self.send_request(url, params)

    def _log(self, response):
        with open(self.build_log_file_path(), 'w+') as f:
            f.write(datetime.datetime.now().date().strftime(
                "%d.%M.%Y") + " --- " + str(response.url) + '\t' + str(response.status_code) + '\t' + json.dumps(
                response.json()) + '\n')
