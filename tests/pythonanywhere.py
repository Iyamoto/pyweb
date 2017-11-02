import unittest
from func_test import TestUrls


class TestPythonAnywhere(TestUrls):
    def setUp(self):
        self.url = 'http://iyamoto.pythonanywhere.com/'

    def test_urls(self):
        self.ping_url(url=self.url)
        self.status_url(url=self.url)
        self.webhook_url(url=self.url)


if __name__ == '__main__':
    unittest.main()
