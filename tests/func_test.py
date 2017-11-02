import unittest
import requests
import subprocess
import time


class MyTestCase(unittest.TestCase):
    def setUp(self):
        cmd = 'docker run -d --name pywebfunctest -p 8080:8080 iyamoto/pyweb:test'
        subprocess.call(cmd, shell=True)
        self.url = 'http://127.0.0.1:8080/'
        time.sleep(2)

    def tearDown(self):
        cmd = 'docker rm -f pywebfunctest'
        subprocess.call(cmd, shell=True)

    def test_ping_url(self):
        url = self.url + 'ping'
        print(url)
        r = requests.get(url)
        print(r.status_code, r.reason, r.ok)
        self.assertEqual(True, r.ok)

    def test_status_url(self):
        url = self.url + 'status'
        print(url)
        r = requests.get(url)
        print(r.status_code, r.reason, r.ok)
        print(r.json())
        self.assertEqual(True, r.ok)

    def test_webhook_url(self):
        url = self.url + 'webhook'
        print(url)
        r = requests.post(url)
        print(r.status_code, r.reason, r.ok)
        self.assertEqual(True, r.ok)

if __name__ == '__main__':
    unittest.main()
