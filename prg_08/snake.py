import numpy as np
import pandas as pd


class Snake:
    ENTITY_INVALID = -1
    ENTITY_ROCK = 4
    ENTITY_FOOD = 3
    ENTITY_SNAKE_BODY = 2
    ENTITY_SNAKE_HEAD = 1
    ENTITY_EMPTY = 0
    MOVEMENT_RIGHT = (+1, 0)
    MOVEMENT_LEFT = (-1, 0)
    MOVEMENT_DOWN = (0, -1)
    MOVEMENT_UP = (0, +1)

    def __init__(self, x_size=20, initial_snake_head_position=(0, 0)):
        y_size = int(x_size * 0.75)
        self.grid = pd.DataFrame(np.zeros(x_size * y_size).reshape((x_size, y_size)))
        self.snake_head_position = initial_snake_head_position

    def get_grid_size(self):
        return self.grid.shape

    def move_snake_head(self, movement):
        current_position = self.get_snake_head_position()
        self.set_snake_head_position((current_position[0] + movement[0], current_position[1] + movement[1]))

    def get_snake_head_position(self):
        return self.snake_head_position

    def set_snake_head_position(self, position):
        success = self.set_entity(Snake.ENTITY_SNAKE_HEAD, position)
        if success:
            # TODO: Do we need to save the snake's head position separately?
            self.snake_head_position = position
        return success

    def __is_valid_position(self, position):
        return self.__is_valid_dimension(self.grid.shape[0], position[0]) and \
               self.__is_valid_dimension(self.grid.shape[1], position[1])

    def __is_valid_dimension(self, expected, actual):
        return 0 <= actual < expected

    def set_entity(self, entity, position):
        if not self.__is_valid_entity(entity) or not self.__is_valid_position(position):
            return False
        self.grid.iloc[position] = entity
        return True

    def get_entity(self, position):
        if self.__is_valid_position(position):
            return self.grid.iloc[position]
        else:
            return Snake.ENTITY_INVALID

    def __is_valid_entity(self, entity):
        # Quick and dirty
        return Snake.ENTITY_EMPTY <= entity <= Snake.ENTITY_ROCK
