import unittest
import requests
import subprocess
import time


class PythonAnywhere(unittest.TestCase):
    def setUp(self):
        self.url = 'http://iyamoto.pythonanywhere.com/'

    def test_urls(self):
        # Test ping url
        url = self.url + 'ping'
        print(url)
        r = requests.get(url)
        print(r.status_code, r.reason, r.ok)
        self.assertEqual(True, r.ok)

        # Test status url
        url = self.url + 'status'
        print(url)
        r = requests.get(url)
        print(r.status_code, r.reason, r.ok)
        print(r.json())
        self.assertEqual(True, r.ok)


if __name__ == '__main__':
    unittest.main()
