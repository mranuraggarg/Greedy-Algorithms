# Uses python3
from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def is_covered(segment, point):
    return segment.start <= point <= segment.end

def optimal_points(segments):
    points = []

    while segments:
        r = min([s.end for s in segments])
        points.append(r)
        segments = [s for s in segments if not is_covered(s, r)]

    return points

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, stdin.readline().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
