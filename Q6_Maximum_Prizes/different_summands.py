# Uses python3
import sys
from math import ceil, sqrt


def max_product(num):
    if num % 2 == 0:
        y1: int = num / 2 - 1
        y2: int = y1 + 2
    else:
        y1 = ceil(num / 2)
        y2 = y1 - 1
    return [y1, y2]


def remove_item(sum_array, res):
    for num in res:
        if num not in sum_array:
            new_res = max_product(num)
            sum_array = remove_item(sum_array, new_res)
        else:
            idx = sum_array.index(num)
            del sum_array[idx]
    return sum_array


def optimal_summands(number: int) -> list:
    """

    :type number: int
    """

    k = ceil(0.5*(sqrt(8*number + 1) - 1)) + 2
    sum_list: list = list(range(1, k))
    while sum(sum_list) > number:
        extra_num = sum(sum_list) - number
        if sum(sum_list) - number >= number:
            sum_list.pop()
        elif extra_num in sum_list:
            idx = sum_list.index(extra_num)
            del sum_list[idx]
        else:
            max_p = max_product(extra_num)
            sum_list = remove_item(sum_list, max_p)
    return sum_list


if __name__ == '__main__':
    in_data = sys.stdin.readline()
    n = int(in_data)
    summands = optimal_summands(n)
    print('Maximum number of prizes are {}'.format(len(summands)))
    print('Number of candies distributed are (Last ----> First): ', *summands, sep=' ')
