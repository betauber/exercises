from epr_04.elevator import Elevator


class Building:
    def __init__(self):
        self.elevator1 = Elevator()
        self.elevator2 = Elevator()

    def call_an_elevator_up(self, callers_floor):
        if self.elevator1.is_idling():
            self.elevator1.call_up(callers_floor)
        elif self.elevator2.is_idling():
            self.elevator2.call_up(callers_floor)
        else:
            self.elevator1.call_up(callers_floor)

    def call_an_elevator_down(self, callers_floor):
        if self.elevator1.is_idling():
            self.elevator1.call_down(callers_floor)
        elif self.elevator2.is_idling():
            self.elevator2.call_down(callers_floor)
        else:
            self.elevator1.call_down(callers_floor)

    def tick_elevators(self):
        pass

    def tack_elevators(self):
        pass
