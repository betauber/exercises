import numpy as np
import pandas as pd
import abc


class PahTumBase(metaclass=abc.ABCMeta):
    STONE_EMPTY = 0
    STONE_PLAYER_1 = 1
    STONE_PLAYER_2 = 2
    POINTS_PER_CHAIN_LENGTH = {3: 3, 4: 10, 5: 25, 6: 56, 7: 119}
    CHAIN_MIN_LENGTH = 3

    @abc.abstractmethod
    def is_game_over(self):
        """
        Checks whether there are free cells for placing stones
        :return: True if so
        """

    @abc.abstractmethod
    def stone_at(self, position):
        """
        :param position: (x,y) tuple
        :return: The stone at the the given position
        """
    @abc.abstractmethod
    def is_empty(self, position):
        """

        :param position:
        :return:
        """

    @abc.abstractmethod
    def count_points(self):
        """

        :return:
        """

    def place_stone(self, stone, position):
        if not self.is_empty(position) or not self._is_valid(stone):
            return False
        else:
            self._set_stone(position, stone)
            return True

    @abc.abstractmethod
    def _set_stone(self, position, stone):
        """
        Note that this is an protected abstract method not meant to be used by clients
        :param position:
        :param stone:
        :return:
        """

    def _is_valid(self, stone):
        # Common protected method validating stones
        return stone == PahTum.STONE_PLAYER_1 or stone == PahTum.STONE_PLAYER_2


class PahTum(PahTumBase):

    def __init__(self):
        self.grid = pd.DataFrame(np.zeros(7 * 7, dtype='int32').reshape((7, 7)))

    def __str__(self):
        return self.grid.__str__()

    def is_game_over(self):
        return PahTum.STONE_EMPTY not in self.grid.values

    def stone_at(self, position):
        return self.grid.iloc[position]

    def is_empty(self, position):
        return self.grid.iloc[position] == PahTum.STONE_EMPTY

    def count_points(self):
        player_1_points = 0
        player_1_points += self.__count_points_for_player_on_axis(player=PahTum.STONE_PLAYER_1, axis=0)
        player_1_points += self.__count_points_for_player_on_axis(player=PahTum.STONE_PLAYER_1, axis=1)
        player_2_points = 0
        player_2_points += self.__count_points_for_player_on_axis(player=PahTum.STONE_PLAYER_2, axis=0)
        player_2_points += self.__count_points_for_player_on_axis(player=PahTum.STONE_PLAYER_2, axis=1)
        return player_1_points, player_2_points

    def __count_points_for_player_on_axis(self, player, axis):
        boolean_grid = self.grid == player
        occurrences = boolean_grid.apply(self.__calc_chains, axis=axis)
        return self.__calc_points_total(occurrences)

    def __calc_chains(self, occurrence):
        chains = []
        i = 0
        while i < occurrence.size:
            chain_length = 0
            while i < occurrence.size and occurrence[i]:
                chain_length += 1
                i += 1
            if chain_length >= PahTumBase.CHAIN_MIN_LENGTH:
                chains.append(chain_length)
            i += 1
        return chains

    def __calc_points_total(self, series_of_lists_of_chains):
        series_of_points = series_of_lists_of_chains.apply(self.__calc_points)
        return series_of_points.sum()

    def __calc_points(self, list_of_chains):
        points = 0
        for chain in list_of_chains:
            points += PahTum.POINTS_PER_CHAIN_LENGTH[chain]
        return points

    def _set_stone(self, position, stone):
        self.grid.iloc[position] = stone



