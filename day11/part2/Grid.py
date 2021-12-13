
class Octopus:
    def __init__(self, energy):
        self.energy = energy
        self.flashed = False

    def step(self):
        self.energy += 1

    def flash(self):
        self.flashed = True

    def get_flashed(self):
        return self.flashed

    def get_energy(self):
        return self.energy

    def reset(self):
        self.energy = 0

    def __str__(self):
        return '%d' % self.energy


class Grid:
    def __init__(self, octopi):
        self.grid = []
        for r in range(10):
            self.grid.append([])
            for c in range(10):
                self.grid[r].append(Octopus(int(octopi[(r * 10) + c])))
        self.steps = 0
        self.flashes = 0

    def step(self):
        flashes = []
        for _ in range(10):
            flashes.append([False]*10)

        # Increase energy level of all octopi by 1
        for r in self.grid:
            for c in r:
                c.step()

        # Propagate energy
        flashed = True
        while flashed:
            flashed = False
            for r_idx, r in enumerate(self.grid):
                for c_idx, c in enumerate(r):
                    if c.energy > 9 and flashes[r_idx][c_idx] == False:
                        flashes[r_idx][c_idx] = True
                        flashed = True
                        self._update_adjacents([c_idx, r_idx])

        # Reset nodes that flashed
        for r_idx, r in enumerate(flashes):
            for c_idx, c in enumerate(r):
                if c == True:
                    self.grid[r_idx][c_idx].reset()
                    self.flashes += 1
        self.steps += 1

    def _update_adjacents(self, origin):
        # Starting at north and moving clockwise
        directions = [[0, 1], [1, 1], [1, 0], [
            1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for d in directions:
            try:
                if origin[1]+d[1] >= 0 and origin[0]+d[0] >= 0:
                    self.grid[origin[1]+d[1]][origin[0]+d[0]].step()
            except:
                pass

    def get_steps(self):
        return self.steps

    def get_flashes(self):
        return self.flashes

    def get_grid(self):
        return self.grid

    def __str__(self):
        s = ''
        for r in self.grid:
            for c in r:
                s += str(c)
            s += '\n'
        return s
