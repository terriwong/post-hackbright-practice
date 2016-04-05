"""
'garden' is a N x M 2D array, each value represents the carrots in that square;
'rabbit' starts from the center;
if there's no exact center point, start from the biggest value nearest the 'center';
everytime rabbit eats up the current square, it moves either up, down, left or right to the biggest value;
assume rabbit doesn't need to struggle between 2 same values.
develop a function that takes in garden and returns the number of carrots the rabbit eats.

sample input:

[[5, 7, 8, 6, 3],
 [0, 0, 7, 0, 4],
 [4, 6, 3, 4, 9],
 [6, 2, 5, 9, 7],
 [3, 1, 0, 5, 8]]

expected output:
30
(3 + 7 + 8 + 7 + 5)

"""

def total_carrots_eaten(garden):
    """Given garden the 2D array, returns total number of carrots the rabbit eats."""

    # N the width; M the height
    N = len(garden[0])
    M = len(garden)

    # determine the starting point
    if N % 2 == 1:
        start_x = (N - 1) / 2
        if M % 2 == 1:
            start_y = (M - 1) / 2
        else:
            if garden[M / 2][start_x] > garden[M / 2 - 1][start_x]:
                start_y = M / 2
            else:
                start_y = M / 2 - 1
    elif N % 2 == 0:
        if M % 2 == 1:
            start_y = (M - 1) / 2
            if garden[start_y][N / 2] > garden[start_y][N / 2 - 1]:
                start_x = N / 2
            else:
                start_x = N / 2 - 1
        else:
            biggest_around_center = find_next_biggest(M / 2, N / 2, [(-1, -1), (-1, 0), (0, -1)], garden)
            start_x, start_y = biggest_around_center[0][1], biggest_around_center[0][0]

    # set counter: start from starting point value
    counter = garden[y][x]
    # set value to 0 as mark of eaten
    garden[y][x] = 0
    # set pointer from starting point
    curr_y = start_y
    curr_x = start_x

    rabbit_goes_sleep = False

    while not rabbit_goes_sleep:

        next = find_next_biggest(curr_y, curr_x, [(0, -1), (0, 1), (-1, 0), (1, 0)], garden)

        # if next biggest value is 0, means no more carrots nearby to eat, rabbit goes to sleep
        if next[1] == 0:
            rabbit_goes_sleep = True

        else:
            # add next biggest value to counter
            counter += next[1]
            # set value to 0 as mark of eaten
            garden[next[0][0], next[0][1]] = 0
            # move current pointer to next square
            curr_x, curr_y = next[0][1], next[0][0]

    return counter


def find_next_biggest(curr_y, curr_x, directions, garden):
    """Determine next biggest value's location represented by (y, x)."""
    current_max = [(curr_y, curr_x), garden[curr_y][curr_x]]
    for y, x in directions:
        if garden[curr_y + y][curr_x + x] > current_max[1] and curr_y + y >= 0 and curr_x + x >= 0:
            current_max = [(y, x), garden[y][x]]
    return current_max

