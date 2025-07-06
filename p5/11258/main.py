import sys

def partition(string):
    print(string)
    pass

if __name__ == '__main__':
    data = sys.stdin.read().split()
    n = int(data[0])
    for i in range(1, n + 1):
        result = partition(data[i])
        print(result)
