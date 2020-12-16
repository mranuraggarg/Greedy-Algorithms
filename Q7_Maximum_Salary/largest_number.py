# uses python3
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
