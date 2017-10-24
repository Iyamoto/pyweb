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
        pingurl = self.url + 'ping'
        print(pingurl)
        r = requests.get(pingurl)
        print(r.status_code, r.reason, r.ok)
        self.assertEqual(True, r.ok)


if __name__ == '__main__':
    unittest.main()
