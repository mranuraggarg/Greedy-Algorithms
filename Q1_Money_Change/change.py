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


def get_change(amount):
    # write your code here
    exact_change: dict = {}
    change = 0
    change += amount // 10
    exact_change[10] = change
    amount %= 10
    change += amount // 5
    exact_change[5] = amount // 5
    amount %= 5
    change += amount
    exact_change[1] = amount
    return change, exact_change


if __name__ == '__main__':
    money = int(sys.stdin.readline())
    numberOfCoins, change_returned = get_change(money)
    print(f'Exact change  = {change_returned}')
    print(f'Number of coins = {numberOfCoins}')
