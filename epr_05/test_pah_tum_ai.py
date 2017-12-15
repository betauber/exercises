import unittest
from unittest_data_provider import data_provider
from epr_05.pah_tum_ai import *


class PahTumAiDumberTest(unittest.TestCase):
    def setUp(self):
        self.game_instance = PahTum()
        self.under_test = PahTumAiDumber(self.game_instance, PahTumBase.STONE_PLAYER_1)

    def test__dummy(self):
        false = 0
        for i in range(100):
            actual = self.under_test.make_play()
            if not actual:
                false += 1


class PahTumAiSophisticatedTest(unittest.TestCase):
    def setUp(self):
        self.game_instance = PahTum()
        self.under_test = PahTumAiSophisticated(self.game_instance, PahTumBase.STONE_PLAYER_1)

    def test__doggo(self):
        self.under_test.make_play()


if __name__ == '__main__':
    unittest.main()
