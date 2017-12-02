import unittest
from epr_04_lift.lift import Lift


class LiftTest(unittest.TestCase):

    def setUp(self):
        self.under_test = Lift(0)  # Floor the lift waits on initially.

    def test__waiting_time__should_be_0(self):
        actual_waiting_time = self.under_test.waiting_time(0)
        self.assertEqual(0, actual_waiting_time)

    def test__waiting_time__should_be_10(self):
        # Asking for waiting time immediately after calling the lift
        self.under_test.call_lift(10)
        actual_waiting_time = self.under_test.waiting_time(10)
        self.assertEqual(10, actual_waiting_time)

    def test__waiting_time__should_be_invalid(self):
        with self.assertRaises(Exception) as context:
            self.under_test.waiting_time(10)
        self.assertTrue(Lift.never_called, str(context.exception))

    def test__waiting_time__should_be_20_due_to_other_caller(self):
        # Two back to back calls
        self.under_test.call_lift(5)
        self.under_test.call_lift(-10)
        actual_waiting_time_of_second_caller = self.under_test.waiting_time(-10)
        self.assertEqual(20, actual_waiting_time_of_second_caller)

    def test__tick__should_reduce_waiting_time_by_one(self):
        passenger_is_on_floor = 10
        self.under_test.call_lift(passenger_is_on_floor)
        self.under_test.tick()
        actual_passenger_waiting_time = self.under_test.waiting_time(passenger_is_on_floor)
        self.assertEqual(9, actual_passenger_waiting_time)

    def test__tick__subsequent_calls_should_reduce_waiting_time_to_zero(self):
        passenger_is_on_floor = 3
        self.under_test.call_lift(passenger_is_on_floor)
        actual_waiting_time = self.under_test.waiting_time(passenger_is_on_floor)
        self.assertEqual(passenger_is_on_floor, actual_waiting_time)
        self.under_test.tick()
        self.under_test.tick()
        self.under_test.tick()
        actual_waiting_time = self.under_test.waiting_time(passenger_is_on_floor)
        self.assertEqual(0, actual_waiting_time)

    def test__tick__waiting_times_with_two_callers(self):
        passenger1_is_on_floor = 3
        passenger2_is_on_floor = -5
        self.under_test.call_lift(passenger1_is_on_floor)
        self.under_test.tick()
        self.under_test.call_lift(passenger2_is_on_floor)
        self.under_test.tick()
        actual_waiting_time_for_passenger1 = self.under_test.waiting_time(passenger1_is_on_floor)
        actual_waiting_time_for_passenger2 = self.under_test.waiting_time(passenger2_is_on_floor)
        self.assertEqual(1, actual_waiting_time_for_passenger1)
        self.assertEqual(9, actual_waiting_time_for_passenger2)

    def test_take_elevator_to__same_floor(self):
        target_floor = 0
        # It might come up that the travel time changes
        actual_travel_time = self.under_test.take_lift_to(target_floor)
        self.assertEqual(0, actual_travel_time)

if __name__ == '__main__':
    unittest.main()
