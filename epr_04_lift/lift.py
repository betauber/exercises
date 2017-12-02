class Lift():
    never_called = 'Never called the lift!'

    def __init__(self, floor=0):
        self.queue = []
        self.current_floor = floor

    def call_lift(self, floor):
        if self.current_floor != floor:
            self.queue.append(floor)

    # def ride_lift_to(self, target_floor):
    #     return abs(self.current_floor - target_floor)

    def tick(self):
        if len(self.queue) == 0:
            return
        difference = self.current_floor - self.queue[0]
        if abs(difference) == 1:    # Approaching target
            self.queue.pop(0)
        if difference < 0:          # Riding up
            self.current_floor += 1
        else:                       # Riding down
            self.current_floor -= 1

    def waiting_time(self, floor_waiting_on):
        if floor_waiting_on == self.current_floor:
            return 0
        if floor_waiting_on not in self.queue:
            raise Exception(Lift.never_called)
        waiting_time = 0
        location = self.current_floor
        queue_iter = iter(self.queue)
        while location != floor_waiting_on:
            target = next(queue_iter)
            waiting_time += abs(location - target)
            location = target
        return waiting_time

    def take_lift_to(self, target_floor):
        if self.current_floor == target_floor:
            return 0
        # We will grant each passenger to take the lift immediately
        # TODO: Change this later / apply rulese
        self.queue.insert(0, target_floor)
        return abs(self.current_floor - target_floor)
