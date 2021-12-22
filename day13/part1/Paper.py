import copy


class Paper:
    def __init__(self, points):
        self.points = {}
        self.length = 0
        max_x = 0
        max_y = 0
        for point in points:
            max_x = max(max_x, point[0])
            max_y = max(max_y, point[1])
            if point[1] not in self.points:
                self.points[point[1]] = {}
            self.points[point[1]][point[0]] = True
            self.length += 1
        self.max_x = max_x
        self.max_y = max_y

    def fold(self, point):

        tmp = copy.deepcopy(self.points)
        removals = []
        # Fold horizontally
        if point[1] == 0:
            line = point[0]
            for y, v in tmp.items():
                for x, _ in v.items():
                    t = line - abs(line-x)
                    if t < 0:
                        removals.append([x, y])
                        continue
                    if x > line:
                        removals.append([x, y])
                        if y not in self.points:
                            self.points[y] = {}
                        self.points[y][t] = True
                    elif x == line:
                        removals.append([x, y])
            self.max_x = line-1

        # Fold vertically
        else:

            line = point[1]
            for y, v in tmp.items():
                for x, _ in v.items():
                    t = line - abs(line-y)
                    if t < 0:
                        removals.append([x, y])
                        continue
                    if y > line:
                        removals.append([x, y])
                        if t not in self.points:
                            self.points[t] = {}
                        self.points[t][x] = True
                    elif y == line:
                        removals.append([x, y])
            self.max_y = line - 1

        # Remove keys
        for r in removals:
            del self.points[r[1]][r[0]]

        return True

    def get_visible_dots(self):
        num = 0
        for _, v in self.points.items():
            for _ in v:
                num += 1
        return num

    def __str__(self):
        s = []
        for _ in range(self.max_y+1):
            for _ in range(self.max_x+1):
                s.append('.')
            s.append('\n')
        for y, v in self.points.items():
            for x, _ in v.items():
                s[(y * self.max_x) + (y * 2) + x] = "#"
        return ''.join(s)

    def __len__(self):
        return self.length
