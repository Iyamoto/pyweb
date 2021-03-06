import unittest
import rnd


class MyTestCase(unittest.TestCase):
    def test_index(self):
        self.assertEqual('<h1>PYWEB</h1>', rnd.index())

    def test_ping(self):
        self.assertEqual('ok', rnd.health())

    def test_status(self):
        self.assertDictEqual({'bottle': 'UP'}, rnd.status())

    def test_webhook(self):
        self.assertEqual(None, rnd.webhook())

    def test_error_404(self):
        self.assertEqual(str, type(rnd.error404()))


if __name__ == '__main__':
    unittest.main()
