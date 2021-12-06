
class LanternFish:
    def __init__(self, timer):
        self.spawn_timer = timer

    def get_spawn_timer(self):
        return self.spawn_timer

    def elapse_day(self):
        if self.spawn_timer == 0:
            self.spawn_timer = 6
            return True
        else:
            self.spawn_timer -= 1
            return False
