# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    no_of_stops = 0
    start = 0
    stops.append(distance)
    for i in range(len(stops) - 1):
        if stops[i] - start <= tank < stops[i+1] - start:
            no_of_stops += 1
            start = stops[i]
            if tank < stops[i+1] - start:
                return -1

    return no_of_stops

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.readline().split())
    print(compute_min_refills(d, m, stops))
