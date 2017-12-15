from epr_05.pah_tum import PahTum, PahTumBase
import abc


class PahTumAiBase(metaclass=abc.ABCMeta):

    def __init__(self, game, stone):
        self.game = game
        self.stone = stone

    @abc.abstractmethod
    def make_play(self):
        """
        TODO
        :return:
        """


class PahTumAiDumber(PahTumAiBase):
    def __init__(self, game, stone):
        super().__init__(game, stone)
        self.arbitrary_position = (0, 0)

    def make_play(self):
        if self.game.is_game_over():
            return False
        while True:
            if self.game.place_stone(self.stone, self.arbitrary_position):
                return True
            self.arbitrary_position = self.__next_arbitrary_position(self.arbitrary_position)
            if self.__all_positions_tried(self.arbitrary_position):
                return False

    def __next_arbitrary_position(self, position):
        x = position[0]
        y = position[1]
        x = (x + 1) % PahTumBase.GAME_GRID_DIMENSION
        if x % PahTumBase.GAME_GRID_DIMENSION == 0:
            y = (y + 1) % PahTumBase.GAME_GRID_DIMENSION
        return x, y

    def __all_positions_tried(self, position):
        return position[0] == position[1] == 0


class PahTumAiSophisticated(PahTumAiBase):
    def make_play(self):
        potential_own_points = self.__calc_potential_points(self.stone)
        potential_player_points = self.__calc_potential_points(self.game.get_other_player(self.stone))

    def __calc_potential_points(self, for_stone):
        return 0
