import math


def calculate_fuel_usage(positions, n):
    fuel_usage = 0
    for p in positions:
        fuel_usage += abs(n-p)
    return fuel_usage


def find_median(positions):
    positions.sort()
    median_pos = math.floor(len(positions)/2)
    return positions[median_pos]
