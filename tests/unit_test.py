import unittest
import rnd


class MyTestCase(unittest.TestCase):
    def test_index(self):
        assert rnd.index() == '<h1>pyweb</h1>'

    def test_ping(self):
        assert rnd.health() == 'ok'

    def test_status(self):
        assert type(rnd.status()) == dict
        assert rnd.status() == {'bottle': 'UP'}


if __name__ == '__main__':
    unittest.main()
