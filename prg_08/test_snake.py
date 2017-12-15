import unittest
from unittest_data_provider import data_provider
from prg_08.snake import Snake


def snake_head_position_data():
    return (
        ((9, 6), Snake.MOVEMENT_LEFT),
        ((4, 3), Snake.MOVEMENT_RIGHT),
        ((2, 13), Snake.MOVEMENT_RIGHT),
        ((5, 2), Snake.MOVEMENT_RIGHT)
    )


def entity_data():
    return (
        (Snake.ENTITY_EMPTY,),
        (Snake.ENTITY_SNAKE_HEAD,),
        (Snake.ENTITY_SNAKE_BODY,),
        (Snake.ENTITY_FOOD,),
        (Snake.ENTITY_ROCK,)
    )


class PahTumTest(unittest.TestCase):
    def setUp(self):
        self.under_test = Snake()

    def test__4_to_3_format(self):
        arbitrary_base_size = 30
        x = 4 * arbitrary_base_size
        y = 3 * arbitrary_base_size
        self.assertTrue(x * 0.75 == y)

    def test__get_grid_size(self):
        # Given
        x_size = 50
        self.under_test = Snake(x_size)
        # When
        actual = self.under_test.get_grid_size()
        # Then
        self.assertTrue(int(actual[0] * 0.75) == actual[1], "%d %d" % (int(actual[0] * 0.75), actual[1]))
        self.assertEqual((x_size, int(x_size * 0.75)), actual)

    def test__place_invalid_snake_head_position(self):
        actual = self.under_test.set_snake_head_position((-1, 100))
        self.assertFalse(actual)

    @data_provider(snake_head_position_data)
    def test__get_snake_head_position(self, snake_head_position, movement):
        self.under_test.set_snake_head_position(snake_head_position)
        actual = self.under_test.get_snake_head_position()
        self.assertEqual(snake_head_position, actual)

    @data_provider(snake_head_position_data)
    def test__move_snake(self, position, movement):
        # Given
        self.under_test.set_snake_head_position(position)
        # When
        self.under_test.move_snake_head(movement)
        actual = self.under_test.get_snake_head_position()
        # Then
        expected = (position[0] + movement[0], position[1] + movement[1])
        self.assertEqual(expected, actual)

    def test__move_snake_invalid(self):
        self.under_test.set_snake_head_position((10, 0))
        actual = self.under_test.move_snake_head(Snake.MOVEMENT_DOWN)
        self.assertFalse(actual)

    @data_provider(entity_data)
    def test__set_and_get_entities(self, entity):
        position = (10, 10)
        set_entity_successful = self.under_test.set_entity(entity, position)
        self.assertTrue(set_entity_successful)
        actual_entity_at_position = self.under_test.get_entity(position)
        self.assertEqual(entity, actual_entity_at_position)


if __name__ == '__main__':
    unittest.main()
