from math import sqrt
from sys import stdin

def get_perms(n):
    perms = []
    def p(n, arr):
        if n == 1:
            perms.append(arr[:])
            return

        p(n - 1, arr)

        for i in range(n - 1):
            if n % 2 == 0:
                arr[i], arr[n-1] = arr[n-1], arr[i]
            else:
                arr[0], arr[n-1] = arr[n-1], arr[0]

            p(n - 1, arr)

    p(n, list(range(n)))

    return perms

def get_box_width(circles):
    n = len(circles)
    # list of maximal distances between circles 
    # where x[i] is the distance from the center of the first circle and the ith circle 
    x = [0.0] * n
    x[0] = 0.0

    for i in range(1, n):
        max_x = -float('inf')
        for j in range(i):

            dist = 2 * sqrt(circles[i] * circles[j])

            # distance that was required to get to the j-th circle + distance between i-th and j-th
            candidate_x = x[j] + dist
            max_x = max(max_x, candidate_x)
        x[i] = max_x

    # for each x get the remaining distance on the left (the "hangover"), get the minimum (which is the maximal hangover)
    left_widths = [x[i] - circles[i] for i in range(n)]
    # get the biggest hangover on the right, as that will be the circle that is actually touching the right side of the box
    right_widths = [x[i] + circles[i] for i in range(n)]

    left = min(left_widths)
    right = max(right_widths)

    # the box width is just the distance between circles + right hangover + left hangover
    # here 'right' is the maximal distance from the center of the first circle to the right side of the box
    # and 'left' is the hangover that has to be added on the left (it is negative so i subtract, or i could also get the absolute value)
    box_width = right - left

    # print(circles, x)
    # print(left_widths, left, right_widths, right)
    # print('--------------------')

    return box_width


def find_box_width_brute(circles):
    width = 1_000_000_000_000_000_000
    # min_config = []

    n = len(circles)

    for perm in get_perms(n):
        config = [circles[i] for i in perm]

        current_width = get_box_width(config)
        if current_width < width:
            width = current_width
            # min_config = config

    return width  #, min_config


if __name__ == "__main__":
    '''
    start and end should be the smallest
    palindromes are equal
    '''

    lines = [line.strip() for line in stdin.readlines()]
    output = []

    for line in lines[1:]:
        numbers = list(map(float, line.split()))
        assert 1 <= numbers[0] <= 8
        circles = numbers[1:]
        min_width = find_box_width_brute(circles)
        output.append("%.3f" % min_width)

    print('\n'.join(output))
        

    # print( get_perms(4) )
    # assert len( get_perms(3) ) == 6
    # assert len( get_perms(4) ) == 24
    # assert len( get_perms(5) ) == 5*24

    # print( find_box_width_brute([1,2,2]) )  # 9.657
    # print( find_box_width_brute([1,2,2]) )  # 16.000
    # print( find_box_width_brute([1,2,4]) )  # 12.657

    # circles = [3,1,2]
    # print( circles, box_width(circles) )
    # circles = [3,2,1]
    # print( circles, box_width(circles) )
    # circles = [3,2,2]
    # print( circles, box_width(circles) )
    # circles = [2,3,2]
    # print( circles, box_width(circles) )
    # circles = [3,2,3]
    # print( circles, box_width(circles) )
    # circles = [3,2.5,3]
    # print( circles, box_width(circles) )
    # circles = [2.5,3,3]
    # print( circles, box_width(circles) )
    # circles = [2,2,4,3]
    # print( circles, box_width(circles) )
    # circles = [3,2,2,4]
    # print( circles, box_width(circles) )
    # circles = [2,3,4,2]
    # print( circles, box_width(circles) )
    # circles = [2,3,3,4,5,4,3,2]
    # print( circles, box_width(circles) )
    # circles = [2,3,4,5,4,3,2]
    # print( circles, box_width(circles) )
    # circles = [2,5,3,4,3,4,2]
    # print( circles, box_width(circles) )

    
