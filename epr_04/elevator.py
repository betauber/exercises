class Elevator:
    def __init__(self, floor=0):
        self.floor = floor
        self.direction = None
        self.queue_in_current_direction = []
        self.queue_in_opposite_direction = []

    def tack(self):
        while not self.is_idling():
            self.tick()

    def tick(self):
        if self.is_riding_up():
            self.floor += 1
        elif self.is_riding_down():
            self.floor -= 1

        if self.floor == self.queue_in_current_direction[0]:
            self.queue_in_current_direction.pop(0)
            # TODO: Elevator arrives at requested floor event

        if self.__has_requests_in_current_direction():
            pass
        elif self.__has_requests_in_opposite_direction():
            self.__turn_and_handle_requests_of_opposite_direction()
        else:
            self.__set_elevator_to_idling()

    def is_riding_up(self):
        return self.direction == 'up'

    def is_riding_down(self):
        return self.direction == 'down'

    def __has_requests_in_current_direction(self):
        return len(self.queue_in_current_direction) > 0

    def __has_requests_in_opposite_direction(self):
        return len(self.queue_in_opposite_direction) > 0

    def __turn_and_handle_requests_of_opposite_direction(self):
        self.queue_in_current_direction = self.queue_in_opposite_direction
        self.queue_in_current_direction.sort(reverse=True) # TODO: OK or not reverse?
        self.queue_in_opposite_direction = []
        self.__switch_direction(self.direction)

    def __set_elevator_to_idling(self):
        assert not self.__has_requests_in_current_direction()
        assert not self.__has_requests_in_opposite_direction()
        self.direction = None

    def ride_to(self, target_floor):
        self.__handle_call(self.__get_direction(), target_floor)

    def call_up(self, callers_floor):
        self.__handle_call('up', callers_floor)

    def call_down(self, callers_floor):
        self.__handle_call('down', callers_floor)

    def __handle_call(self, direction ,callers_floor):
        if callers_floor == self.floor:
            return
        if self.__can_handle_request_without_turning(direction, callers_floor):
            self.__add_floor_request_in_direction(callers_floor)
        else:
            self.__add_floor_request_in_opposite_direction(callers_floor)

    def __can_handle_request_without_turning(self, callers_direction, callers_floor):
        if self.is_idling():
            self.__set_direction(callers_direction)
            return True
        else:
            return callers_direction == self.direction and self.floor < abs(callers_floor)  # TODO: Verify if correct

    def is_idling(self):
        return self.__get_direction() is None and not self.__has_requests_in_current_direction() and not self.__has_requests_in_opposite_direction()

    def __add_floor_request_in_direction(self, floor):
        self.queue_in_current_direction.append(floor)
        self.queue_in_current_direction.sort()

    def __add_floor_request_in_opposite_direction(self, floor):
        self.queue_in_opposite_direction.append(floor)

    def __set_direction(self, direction):
        self.direction = direction

    def __switch_direction(self, old_direction):
        if self.__get_direction() == 'up':
            self.__set_direction('down')
        elif self.__get_direction() == 'down':
            self.__set_direction('up')
        else:
            raise Exception("Cannot switch direction if direction is %o" % self.__get_direction())

    def __get_direction(self):
        return self.direction
