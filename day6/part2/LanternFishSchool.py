class LanternFishSchool:
    def __init__(self, fish):
        self.days_elapsed = 0
        self.school_length = 0
        self.school = [0] * 9
        for f in fish:
            self.school[int(f)] += 1
            self.school_length += 1

    def elapse_day(self):
        # Move fish to new bucket
        new_school = [0] * 9
        for idx, fish in enumerate(self.school):
            if idx == 0:
                new_school[6] += fish
                new_school[8] += fish
                self.school_length += fish
            else:
                new_school[idx-1] += self.school[idx]
        self.school = new_school
        self.days_elapsed += 1
        return True

    def get_school(self):
        return self.school

    def __len__(self):
        return self.school_length
