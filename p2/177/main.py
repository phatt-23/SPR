import sys

def paper_fold(num):
    '''
    0 -> right
    1 -> up
    2 -> left
    3 -> down

    rotate to right
    right -> up   (0 -> 1)
    up -> left    (1 -> 2)
    left -> down  (2 -> 3)
    down -> right (3 -> 0)
    '''
    right, up, left, down = 0,1,2,3

    def pf(num):
        if num == 0:
            return [right]

        return pf(num - 1) + [(direction + 1) % 4 for direction in list(reversed(pf(num - 1)))]

    path = pf(num)

    # get dimensions
   
    x, y = 0, 0
    bounds_x = [0,0]
    bounds_y = [0,0]
    
    for i,direction in enumerate(path):
        if direction == right:
            if i-1 >= 0 and path[i-1] in (up, down):
                x += 1
            x += 1
        elif direction == left:
            if i-1 >= 0 and path[i-1] in (up, down):
                x -= 1
            x -= 1

        bounds_x[0], bounds_x[1] = min(bounds_x[0], x), max(bounds_x[1], x)

        if direction == up:
            y += 1
        elif direction == down:
            y -= 1

        bounds_y[0], bounds_y[1] = min(bounds_y[0], y), max(bounds_y[1], y)

    # print('NUM:', num)
    # print(path)

    dim_x = bounds_x[1] + (-bounds_x[0]) + 1
    dim_y = bounds_y[1] + (-bounds_y[0]) + 1

    # print('X:', bounds_x, dim_x)
    # print('Y:', bounds_y, dim_y)

    canvas = [' '] * dim_x * dim_y
    canvas = [canvas[i:i+dim_x] for i in range(0, dim_x * dim_y, dim_x)]   

    y = bounds_y[1]
    x = -bounds_x[0]

    # print(y, x)

    canvas[y][x] = 'S'

    for i,direction in enumerate(path):
        if direction == right:
            if i-1 >= 0 and path[i-1] in (up, down):
                x += 1
            canvas[y][x] = '_'
            x += 1
        elif direction == left:
            if i-1 >= 0 and path[i-1] in (up, down):
                x -= 1
            canvas[y][x] = '_'
            x -= 1
        elif direction == up:
            canvas[y][x] = '|'
            y -= 1
        elif direction == down:
            y += 1
            canvas[y][x] = '|'

    return canvas

if __name__ == "__main__":
    numbers = [int(line.strip()) for line in sys.stdin.readlines()]

    for number in numbers:
        if number == 0:
            break

        # assert 1 <= number <= 13

        canvas = paper_fold(number)
        for row in canvas:
            if (''.join(row)).isspace():
                continue
            print(''.join(row).rstrip())
        print('^')

