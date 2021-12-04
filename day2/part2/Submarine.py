class Submarine:
    # Submarine horizontal axis
    # Increases as submarine moves forward
    x = 0

    # Submarine depth
    # Increases as submarine goes down
    y = 0

    # Submarine aim
    aim = 0

    def __init__(self):
        return

    def move(self, direction, units):
        if direction == 'forward':
            self.x += units
            self.y += self.aim * units
        elif direction == 'up':
            self.aim -= units
        elif direction == 'down':
            self.aim += units
        else:
            None

    def get_position(self):
        return [self.x, self.y]

    def get_aim(self):
        return self.aim
