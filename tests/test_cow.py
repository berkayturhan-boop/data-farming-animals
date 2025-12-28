import unittest
from farm.cow import Cow

class TestCow(unittest.TestCase):
    def setUp(self):
        self.cow = Cow()

    def test_talk(self):
        # İneğin konuşması doğru mu?
        self.assertEqual(self.cow.talk(), "Mööö")

    def test_feed(self):
        # İnek beslenince enerjisi artıyor mu?
        self.cow.feed()
        self.assertEqual(self.cow.energy, 1)