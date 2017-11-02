import unittest
import requests


class TestUrls(unittest.TestCase):
    def ping_url(self, url=''):
        url = url + 'ping'
        print(url)
        r = requests.get(url)
        print(r.status_code, r.reason, r.ok)
        self.assertEqual(True, r.ok)

    def status_url(self, url=''):
        url = url + 'status'
        print(url)
        r = requests.get(url)
        print(r.status_code, r.reason, r.ok)
        print(r.json())
        self.assertEqual(True, r.ok)

    def webhook_url(self, url=''):
        url = url + 'webhook'
        print(url)

        data = {'key': 'value'}
        r = requests.post(url, json=data)

        print(r.status_code, r.reason, r.ok)
        self.assertEqual(True, r.ok)
        self.assertDictEqual(data, r.json())
