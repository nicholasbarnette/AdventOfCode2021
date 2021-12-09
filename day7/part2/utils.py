import math


def calculate_fuel_usage(positions, n):
    fuel_usage = 0
    for p in positions:
        distance = abs(n-p)
        for d in range(distance):
            fuel_usage += d+1
    return fuel_usage


def find_mean(positions):
    position_sum = 0
    for p in positions:
        position_sum += p
    return math.floor(position_sum / len(positions))


def find_median(positions):
    positions.sort()
    median_pos = math.floor(len(positions)/2)
    return positions[median_pos]
