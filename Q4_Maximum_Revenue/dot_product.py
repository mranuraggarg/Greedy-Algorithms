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


def multi(x):
    return x[0] * x[1]


def max_dot_product(x, y):
    # write your code here
    return sum((map(multi, zip(x, y))))


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = sorted(data[1:(n + 1)], reverse=True)
    b = sorted(data[(n + 1):], reverse=True)
    print('Maximum revenue is {}'.format(max_dot_product(a, b)))
