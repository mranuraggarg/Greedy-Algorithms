# uses python3
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


def is_better(x, y) -> bool:
    return int(x + y) > int(y + x)


def largest_number(lst) -> str:
    # write your code here
    res = ""
    while lst:
        max_number = '0'
        num: str
        for num in lst:
            if is_better(num, max_number):
                max_number = num
        res += max_number
        idx = lst.index(max_number)
        del lst[idx]
    return res


if __name__ == '__main__':
    input_data = sys.stdin.readline()
    data = input_data.split()
    print('The maximum possible salary is: {}'.format(largest_number(data)))
