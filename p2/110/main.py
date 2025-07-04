import sys
import string
from pprint import pprint

SPACE = '    '

def meta_sort(n):
    var = "abcdefgh"
    order = [''] * n
    order[0] = var[0]

    def meta_sort_imp(idx, n):
        if idx == n:
            print(SPACE*idx, f"writeln({','.join(list(reversed(order)))})")
            return
        
        for i in range(idx,0,-1):
            order[i] = order[i-1]

        print(SPACE*idx, end=' ')

        for i in range(0,idx):
            print('if', order[i+1], '<', var[idx], 'then') 
            order[i] = var[idx]
            meta_sort_imp(idx+1, n)
            order[i] = order[i+1]
            print(SPACE*idx, 'else', end=' ')

            if i == idx - 1:
                print()
                order[i+1] = var[idx]
                meta_sort_imp(idx+1, n)

    meta_sort_imp(1,n)

def meta_sort2(n):
    var = "abcdefgh"
    order = [''] * n
    order[0] = var[0]

    def meta_sort_imp(idx, n, d=0):
        print('\t'*d, 'idx =', idx, 'n =', n)
        if idx == n:
            print('\t'*d, 'OUTPUT', ','.join(list(reversed(order))))
            return
        
        for i in range(idx,0,-1):
            print('\t'*d, f'order[i = {i}] =', order[i], '<-', f'order[i-1 = {i-1}] =', order[i-1])
            order[i] = order[i-1]

        for i in range(0,idx):
            print('\t'*d, order)
            print('\t'*d, f'order[{i}] =', order[i], '<-', f'var[idx = {idx}] =', var[idx])
            order[i] = var[idx]
            print('\t'*d, order)

            meta_sort_imp(idx+1, n, d+1)

            print('\t'*d, f'order[i = {i}] =', order[i], '<-', f'order[i+1 = {i+1}] =', order[i+1]) 
            order[i] = order[i+1]

            if i == idx - 1:
                order[i+1] = var[idx]
                meta_sort_imp(idx+1, n, d+1)

    meta_sort_imp(1,n)

def meta_sort3(n):
    assert 0 <= n <= 8
    select = list(reversed(range(n)))
    select.insert(0, select.pop())

    def meta(idx, n):
        print('*'*idx, idx, select)
        if idx == n:
            print(' '*idx, 'base')
            return
        
        # shift everything to the right
        select.insert(0, select.pop())

        print(' '*idx, 'shift', select)

        for i in range(0,idx):
            assert select[i] == idx
            # print(' '*idx, 'if', select[i+1], '<', select[i], 'then') 
            meta(idx+1, n)

            # swap positions
            select[i], select[i+1] = select[i+1], select[i]
            print(' '*idx, 'swap', i, i+1, select)
            assert select[i] != ''

            # last iteration
            if i == idx - 1:
                assert i+1 == idx
                assert select[i+1] == idx
                print(' '*idx, 'last')
                meta(idx+1, n)

    meta(1,n)

def meta_sort4(n):
    assert 0 <= n <= 8
    select = list(reversed(range(n)))
    select.insert(0, select.pop())
    space = '    '

    def meta(idx, n):
        if idx == n:
            vars = ','.join(string.ascii_lowercase[i] for i in list(reversed(select)))
            print(f'{space*idx}writeln({vars})')
            return
        
        # shift everything to the right
        select.insert(0, select.pop())

        for i in range(0,idx):
            print(f'{space*idx}if {string.ascii_lowercase[select[i+1]]} < {string.ascii_lowercase[select[i]]} then') 
            meta(idx+1, n)

            # swap positions
            select[i], select[i+1] = select[i+1], select[i]

            print(f'{space*idx}else')

            # last iteration
            if i == idx - 1:
                meta(idx+1, n)

    meta(1,n)


def main():
    numbers = [int(line.strip()) for line in sys.stdin.readlines() if line.strip() != '']
    if len(numbers) <= 0:
        return

    m = numbers[0]

    for i in range(0,m):
        if i != 0:
            print()

        n = numbers[i+1]

        vars = ','.join(string.ascii_lowercase[:n])

        print('program sort(input,output);')
        print('var')
        print(f'{vars} : integer;')
        print('begin')
        print(f'    readln({vars});')
        meta_sort4(n)
        print('end.')
        


if __name__ == "__main__":
    main()

