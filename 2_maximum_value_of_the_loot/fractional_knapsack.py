# Uses python3
import sys

def div(x):
    return x[0]/x[1]
def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    units = list(map(div, zip(values, weights)))
    index = list(range(len(values)))
    index.sort(key=lambda i: units[i], reverse=True)
    for i in index:
        if 0 <= weights[i] <= capacity:
            value += values[i]
            capacity -= weights[i]
        else:
            value += capacity * units[i]
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.readline().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.3f}".format(opt_value))
