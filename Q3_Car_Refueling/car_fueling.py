# python3
import sys


def compute_min_refills(distance, tank, pumps: list):
    """

    :type tank: int
    :type distance: int
    :type pumps: list
    """
    # write your code here
    no_of_stops = 0
    start = 0
    pumps.append(distance)
    exact_stops = {}
    for i in range(len(pumps) - 1):
        if pumps[i] - start <= tank < pumps[i + 1] - start:
            no_of_stops += 1
            start = pumps[i]
            exact_stops['stop ' + str(no_of_stops)] = pumps[i]
            if tank < pumps[i + 1] - start:
                return -1, {'stop 1': None}

    return no_of_stops, exact_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    noOfStops, stoppages = compute_min_refills(d, m, stops)
    if noOfStops == -1:
        print(f'Journey cannot be completed')
    else:
        print(f'Number of stops required are {noOfStops}')
        print(f"Car should be refilled at {stoppages}")
