from LanternFish import LanternFish


class LanternFishSchool:

    def __init__(self, fish):
        self.days_elapsed = 0
        self.school = []
        for f in fish:
            self.school.append(LanternFish(int(f)))

    def elapse_day(self):
        births = 0
        for fish in self.school:
            birth = fish.elapse_day()
            if birth == True:
                births += 1
        for _ in range(births):
            self.school.append(LanternFish(8))
        self.days_elapsed += 1
        return True

    def get_school(self):
        return self.school

    def __len__(self):
        return len(self.school)

    def __str__(self):
        s = "After %d day(s): " % self.days_elapsed
        for idx, fish in enumerate(self.school):
            s += str(fish.get_spawn_timer())
            if idx < len(self.school)-1:
                s += ','
        return s
