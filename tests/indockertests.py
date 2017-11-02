import unittest
import subprocess
import time
from func_test import TestUrls


class TestUrlsInDocker(TestUrls):
    def setUp(self):
        cmd = 'docker run -d --name pywebfunctest -p 8080:8080 iyamoto/pyweb:test'
        subprocess.call(cmd, shell=True)
        self.url = 'http://127.0.0.1:8080/'
        time.sleep(2)

    def tearDown(self):
        cmd = 'docker rm -f pywebfunctest'
        subprocess.call(cmd, shell=True)

    def test_urls(self):
        self.ping_url(url=self.url)
        self.status_url(url=self.url)
        self.webhook_url(url=self.url)


if __name__ == '__main__':
    unittest.main()
