
class SurfaceMap:

    def __init__(self):
        # { "y": { "x": n } }
        self.hydrothermal_vents = {}
        self.length = 0
        return

    def get_points(self, pair):
        [p1, p2] = pair.split(' -> ')
        [p1_x, p1_y] = p1.split(',')
        [p2_x, p2_y] = p2.split(',')
        return [int(p1_x), int(p1_y), int(p2_x), int(p2_y)]

    def add_vent(self, line):
        [p1_x, p1_y, p2_x, p2_y] = self.get_points(line)

        # Vertical line
        if p1_x == p2_x:
            for y in range(min(p1_y, p2_y), max(p1_y, p2_y)+1):
                # Add the x axis record if no dictionary exists yet
                if str(y) not in self.hydrothermal_vents:
                    self.hydrothermal_vents[str(y)] = {}

                # Add the point if it doesn't exist or increment the value at that point
                if str(p1_x) not in self.hydrothermal_vents[str(y)]:
                    self.hydrothermal_vents[str(y)][str(p1_x)] = 1
                else:
                    self.hydrothermal_vents[str(y)][str(p1_x)] += 1
            self.length += 1

        # Horizontal line
        elif p1_y == p2_y:
            for x in range(min(p1_x, p2_x), max(p1_x, p2_x)+1):
                # Add the x axis record if no dictionary exists yet
                if str(p1_y) not in self.hydrothermal_vents:
                    self.hydrothermal_vents[str(p1_y)] = {}

                # Add the point if it doesn't exist or increment the value at that point
                if str(x) not in self.hydrothermal_vents[str(p1_y)]:
                    self.hydrothermal_vents[str(p1_y)][str(x)] = 1
                else:
                    self.hydrothermal_vents[str(p1_y)][str(x)] += 1
            self.length += 1

    def get_max(self):
        k_y = self.hydrothermal_vents.keys()
        max_x = -1
        max_y = -1
        for y in k_y:
            if int(y) > max_y:
                max_y = int(y)
            k_x = self.hydrothermal_vents[y].keys()
            for x in k_x:
                if int(x) > max_x:
                    max_x = int(x)

        return [max_x, max_y]

    def __str__(self):
        [max_x, max_y] = self.get_max()
        s = ""
        for y in range(0, max_y+1):
            if str(y) in self.hydrothermal_vents:
                for x in range(0, max_x+1):
                    if str(x) in self.hydrothermal_vents[str(y)]:
                        s += str(self.hydrothermal_vents[str(y)][str(x)])
                    else:
                        s += "."
            else:
                s += '.' * (max_x+1)
            s += '\n'
        return s

    def __len__(self):
        return self.length
