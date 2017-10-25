import unittest
import rnd


class MyTestCase(unittest.TestCase):
    def test_ping(self):
        assert rnd.health() == 'ok'


if __name__ == '__main__':
    unittest.main()
