
def find_basins(flow_map):
    basins = []
    for r_idx, row in enumerate(flow_map):
        for s_idx, space in enumerate(row):
            is_low = True
            # North, South, East, West | (x,y)
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for d in directions:
                try:
                    if int(space) >= int(flow_map[r_idx + d[0]][s_idx + d[1]]):
                        is_low = False
                except:
                    pass
            if is_low == True:
                basins.append(discover_basins(flow_map, [r_idx, s_idx]))
    return basins


def create_point(point):
    return '(%d,%d)' % (point[0], point[1])


def discover_basins(flow_map, origin):
    coords = set([create_point(origin)])

    queue = [origin]
    while len(queue) > 0:
        current_point = queue.pop(0)
        coords.add(create_point(current_point))
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        for d in directions:
            try:
                point = [current_point[0] + d[0], current_point[1] + d[1]]
                if point[0] >= 0 and point[1] >= 0:
                    if int(flow_map[point[0]][point[1]]) != 9 and create_point(point) not in coords:
                        queue.append(point)
            except:
                pass

    return len(coords)
