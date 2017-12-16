import numpy as np
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
        self.under_test = PahTum(blocked_stone_count=0)

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

    def test__is_valid_position(self):
        actual = self.under_test._is_valid_position((3, 3))
        self.assertTrue(actual)
        actual = self.under_test._is_valid_position((3, -1))
        self.assertFalse(actual)

    def test__tuple_from_ndarray(self):
        size_two_ndarray = np.random.randint(PahTum.GAME_GRID_DIMENSION, size=2)
        tuple_from_ndarray = tuple(size_two_ndarray)
        self.assertEqual(tuple, type(tuple_from_ndarray))
        self.assertEqual(2, len(tuple_from_ndarray))

    def test__place_blocked_stones(self):
        self.under_test = PahTum()
        # blocked_stone_count = 5
        # print(self.under_test)
        # self.under_test._place_blocked_stones(blocked_stone_count)
        # print(self.under_test)

    def test__calc_points(self):
        player_1_tiles = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 6), (1, 7), (1, 8), (1, 9), (3, 0), (3, 1), (3, 4)]
        player_1_points = self.calc_points(player_1_tiles)
        print(player_1_points)

        # Same for player 2

    def calc_points(self, player_tiles):
        row_axis = 0
        column_axis = 1
        player_chains = []
        player_chains.extend(self.calc_chains_per_axis(player_tiles, row_axis))
        player_chains.extend(self.calc_chains_per_axis(player_tiles, column_axis))
        player_points = self.calc_points_from_chains(player_chains)
        return player_points

    def calc_chains_per_axis(self, tiles, axis):
        chains = []
        chain = 1
        i = 0
        player_tile_count = len(tiles)
        while i < player_tile_count - 1:
            i += 1
            if self.tile_on_same_axis(tiles[i - 1], tiles[i], axis) \
                    and self.consecutive_tiles(tiles[i - 1], tiles[i], self.flip_axis(axis)):
                chain += 1
                self.is_last_tile(chain, chains, i, player_tile_count)
            else:
                chains.append(chain)
                chain = 1
                self.is_last_tile(chain, chains, i, player_tile_count)

        return chains

    def is_last_tile(self, chain, chains, i, player_tile_count):
        if i == player_tile_count - 1:
            chains.append(chain)

    def tile_on_same_axis(self, tile1, tile2, axis):
        return tile1[axis] == tile2[axis]

    def consecutive_tiles(self, tile1, tile2, axis):
        return tile1[axis] + 1 == tile2[axis]

    def flip_axis(self, axis):
        return 1 if axis == 0 else 0

    def calc_points_from_chains(self, player_chains):
        points = 0
        points_per_chain_length = {1: 0, 2: 0, 3: 3, 4: 10, 5: 25, 6: 56, 7: 119}
        for chain in player_chains:
            points += points_per_chain_length[chain]
        return points

    def test__print_grid(self):
        cell_content = {(0, 0): "X"}
        grid = self.draw_grid(cell_content)
        # print(grid)

    def draw_grid(self, cell_content):
        row_string = "\n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |\n"
        for row in range(7):
            row_string += str(row)
            for column in range(7):
                row_string += "| "
                row_string += self.parse_cell_content(row, column, cell_content)
                row_string += " "
            row_string += "|\n"
        return row_string

    def parse_cell_content(self, row, column, cell_content):
        if (row, column) in cell_content:
            return cell_content[(row, column)]
        else:
            return " "


if __name__ == '__main__':
    unittest.main()
