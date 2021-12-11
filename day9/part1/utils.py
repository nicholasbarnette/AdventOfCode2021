
def find_low_points(flow_map):
    low_point_risk = 0
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
                low_point_risk += int(space)+1
    return low_point_risk
