import requests

from django.conf import settings


class Bitrix24:
    webhook_url = getattr(settings, 'BITRIX_WEBHOOK_URL', '')

    def build_url(self, method):
        return self.webhook_url + str(method)

    def send_request(self, url, params):
        response = requests.post(url, json=params)
        try:
            return response.json()
        except:
            return response.status_code

    def call_method(self, method, params):
        url = self.build_url(method)
        return self.send_request(url, params)
