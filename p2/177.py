import sys

"""
0 -> right
1 -> up
2 -> left
3 -> down

rotate to right
right   -> up   (0 -> 1)
up      -> left    (1 -> 2)
left    -> down  (2 -> 3)
down    -> right (3 -> 0)
"""

RIGHT, UP, LEFT, DOWN = 0,1,2,3

def rotate_right(dir):
    return (dir + 1) % 4

def paper_fold(num):
    # get path
    def pf(num):
        if num == 0:
            return [RIGHT]

        subp = pf(num - 1)
        return subp + [rotate_right(dir) for dir in reversed(subp)]

    path = pf(num)
   
    # get dimensions
    x, y = 0, 0
    bounds_x = [0,0]
    bounds_y = [0,0]
    
    for i,dir in enumerate(path):
        if dir == RIGHT:
            x += 1
            # prev dir was UP or DOWN, then increment once more
            if i-1 >= 0 and path[i-1] in (UP, DOWN):  
                x += 1
        elif dir == LEFT:
            x -= 1
            # prev dir was UP or DOWN, then decrement once more
            if i-1 >= 0 and path[i-1] in (UP, DOWN):
                x -= 1

        # Y coord is simply
        if dir == UP:
            y += 1
        elif dir == DOWN:
            y -= 1

        # update bounds, gets ever larger
        bounds_x[0], bounds_x[1] = min(bounds_x[0], x), max(bounds_x[1], x)
        bounds_y[0], bounds_y[1] = min(bounds_y[0], y), max(bounds_y[1], y)

    # calculate dimensions and create canvas
    dim_x = bounds_x[1] + (-bounds_x[0]) + 1
    dim_y = bounds_y[1] + (-bounds_y[0]) + 1

    canvas = [' '] * dim_x * dim_y  # make m*n array
    canvas = [canvas[i:i+dim_x] for i in range(0, dim_x * dim_y, dim_x)]  # split the array by dim_x chunks

    # starting coords
    y = bounds_y[1]
    x = -bounds_x[0]

    # canvas[y][x] = 'S'

    for i,dir in enumerate(path):
        if dir == RIGHT:
            if i-1 >= 0 and path[i-1] in (UP, DOWN):
                x += 1
            canvas[y][x] = '_'
            x += 1
        elif dir == LEFT:
            if i-1 >= 0 and path[i-1] in (UP, DOWN):
                x -= 1
            canvas[y][x] = '_'
            x -= 1
        elif dir == UP:
            canvas[y][x] = '|'
            y -= 1
        elif dir == DOWN:
            y += 1
            canvas[y][x] = '|'

    return canvas

if __name__ == "__main__":
    numbers = [int(line.strip()) for line in sys.stdin.readlines()]

    for number in numbers:
        if number == 0:
            break

        assert 1 <= number <= 13

        canvas = paper_fold(number)
        for row in canvas:
            if (''.join(row)).isspace():
                continue
            print(''.join(row).rstrip())
        print('^')


