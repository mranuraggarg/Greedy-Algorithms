# Uses python3
##################################################
## For detail refer README.md in the main folder
##################################################
## GNU General Public License v3.0
##################################################
## Author: ANURAG GARG
## Copyright: Copyright 2020, Greedy Algorithm

## Credits: Kulikov, Alexander S.; Pevzner, Pavel.
# Learning Algorithms Through Programming and Puzzle Solving.
# Active Learning Technologies. Kindle Edition.

## License: GNU GPL v3.0
## Version: 1.1.0
## Mmaintainer: ANURAG GARG
## Email: mranuraggarg@yahoo.com
## Status: stable
####################################################################################################
import sys
from collections import namedtu

Segment = namedtuple('Segment', 'start end')


def is_covered(segment, point):
    return segment.start <= point <= segment.end


def optimal_points(line):
    """

    :type line: list
    """
    points = []

    while line:
        r = min([s.end for s in line])
        points.append(r)
        line = [s for s in line if not is_covered(s, r)]

    return points


if __name__ == '__main__':
    n, *data = map(int, sys.stdin.read().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    pnts = optimal_points(segments)
    print('Lanlord will have to visit {} time(s) to collect all the signatures'.format(len(pnts)))
    if len(pnts) > 1:
        print('Lanlord should visit at ')
        print(*pnts, sep=' and ')
    else:
        print('Lanlord should visit at ', *pnts)
