# Uses python3

def get_change(m):
    #write your code here
    change = 0
    change += m // 10
    m %= 10
    change += m // 5
    m %= 5
    change += m
    return change

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
