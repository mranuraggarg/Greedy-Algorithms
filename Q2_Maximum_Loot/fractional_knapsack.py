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


def div(x):
    return x[0] / x[1]


def get_optimal_value(cap, quantity, val):
    """

    :type quantity: int
    :type val: int
    :type cap: int
    """
    value = 0.
    # write your code here
    units = list(map(div, zip(val, quantity)))
    index = list(range(len(val)))
    index.sort(key=lambda z: units[z], reverse=True)
    for i in index:
        if 0 <= quantity[i] <= cap:
            value += val[i]
            cap -= quantity[i]
        else:
            value += cap * units[i]
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("The total amount of loot is {:.2f}".format(opt_value))
