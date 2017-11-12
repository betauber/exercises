import unittest
import epr_03.dice_game as dg

class TestDiceGame(unittest.TestCase):

    def test_roll_die(self):
        roll = dg.roll_die()
        self.assertTrue(1 <= roll <= 6)

    def test_roll_dice(self):
        rolls = dg.roll_dice(1000)
        self.assertEqual(1000, len(rolls))

    def test_count_of_specific_element_in_list(self):
        element = 1
        n = 1000
        # create a list of half 0's half 1's
        list_of_elemnts = [x % 2 for x in range(n)]
        count_of_element = list_of_elemnts.count(element)
        self.assertEqual(n/2, count_of_element)

    def test_occurence_of_one_element(self):
        element = 4
        n = 600
        faces = 6
        confidence_interval = .05
        actual_deviation_in_percent = self.calc_actual_deviation(element, n, faces)

        self.assertTrue(actual_deviation_in_percent < confidence_interval)

    def calc_actual_deviation(self, element, n, faces):
        expected_count_of_each_outcome = n / faces
        rolls = dg.roll_dice(n,faces)
        count_of_element = rolls.count(element)
        absolute_difference = abs(expected_count_of_each_outcome - count_of_element)
        actual_deviation_in_percent = absolute_difference / n
        return actual_deviation_in_percent

    def test_occurence_of_each_element(self):
        n = 600
        face_count = 10
        confidence_interval = .05
        for face in range(1,face_count+1):
            deviation_of_face = self.calc_actual_deviation(face, n, face_count)
            self.assertTrue(deviation_of_face < confidence_interval, 'Face: ' + str(face) + ' Deviation: ' + str(deviation_of_face))

    def test_random_seed(self):
        count = 10
        seed = 1212121
        faces = 6
        rolls1 = dg.roll_dice(count, faces, seed)
        rolls2 = dg.roll_dice(count, faces, seed)
        self.assertEqual(rolls1, rolls2)

if __name__ == '__main__':
    unittest.main()
