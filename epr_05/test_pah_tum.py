import unittest
from unittest_data_provider import data_provider
from epr_05.pah_tum import PahTum


class PahTumTest(unittest.TestCase):
    stones_for_players = lambda: (
        ((0, 0), PahTum.STONE_PLAYER_1),
        ((0, 1), PahTum.STONE_PLAYER_1),
        ((0, 3), PahTum.STONE_PLAYER_2)
    )

    def setUp(self):
        self.under_test = PahTum()

    def test__grid_is_empty(self):
        self.assertTrue(self.under_test.is_empty((0, 0)))

    def test__is_not_game_over(self):
        self.assertFalse(self.under_test.is_game_over())

    @data_provider(stones_for_players)
    def test__place_stone_for_player(self, stone_position, player):
        # When
        self.under_test.place_stone(player, stone_position)
        # Then
        self.assertFalse(self.under_test.is_empty(stone_position))
        self.assertEqual(player, self.under_test.stone_at(stone_position))


if __name__ == '__main__':
    unittest.main()
