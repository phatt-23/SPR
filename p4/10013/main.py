import sys

read = sys.stdin.read
write = sys.stdout.write

a = [0] * 1_000_000
b = [0] * 1_000_000
c = ['0'] * 1_000_000  

def solve(m):
    carry = 0
    for i in range(m - 1, -1, -1):
        r = a[i] + b[i] + carry
        carry = r // 10
        c[i] = chr((r % 10) + 48)  # ord('0') = 48
    return ''.join(c[:m])

if __name__ == "__main__":
    data = read().split()
    idx = 0
    T = int(data[idx])
    idx += 1

    res = []

    for case in range(T):
        m = int(data[idx])
        idx += 1

        for i in range(m):
            a[i] = int(data[idx])
            b[i] = int(data[idx + 1])
            idx += 2

        res.append(solve(m))

    write('\n\n'.join(res) + '\n')
