class Submarine:
    # Submarine horizontal axis
    # Increases as submarine moves forward
    x = 0

    # Submarine depth
    # Increases as submarine goes down
    y = 0

    def __init__(self):
        return

    def move(self, direction, units):
        if direction == 'forward':
            self.x += units
        elif direction == 'up':
            self.y -= units
        elif direction == 'down':
            self.y += units
        else:
            None

    def get_position(self):
        return [self.x, self.y]
