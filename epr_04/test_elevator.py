import unittest
from epr_04.elevator import Elevator

class ElevatorTest(unittest.TestCase):

    def setUp(self):
        self.under_test = Elevator(0)  # Floor the lift waits on initially.


if __name__ == '__main__':
    unittest.main()
