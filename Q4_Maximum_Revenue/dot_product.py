# Uses python3
import sys


def multi(x):
    return x[0] * x[1]


def max_dot_product(x, y):
    #write your code here
    return sum((map(multi, zip(x, y))))


if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]
    a = sorted(data[1:(n + 1)], reverse=True)
    b = sorted(data[(n + 1):], reverse=True)
    print(max_dot_product(a, b))
    