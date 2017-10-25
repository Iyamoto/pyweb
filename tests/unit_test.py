import unittest
import rnd


class MyTestCase(unittest.TestCase):
    def test_index(self):
        self.assertEqual('<h1>pyweb</h1>', rnd.index())

    def test_ping(self):
        self.assertEqual('ok', rnd.health())

    def test_status(self):
        self.assertDictEqual({'bottle': 'UP'}, rnd.status())


if __name__ == '__main__':
    unittest.main()
