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
            potential_center_points = [(M / 2 - 1, N / 2 - 1), (M / 2 - 1, N / 2), (M / 2, N / 2), (M / 2, N / 2 - 1)]
            current_max = [(0, 0), 0]
            for y, x in potential_center_points:
                if garden[y][x] > current_max[1]:
                    current_max = [(y, x), garden[y][x]]
            start_x, start_y = current_max[0][1], current_max[0][0]

    # set counter: start from starting point value
    counter = garden[y][x]
    # set value to 0 as mark of eaten
    garden[y][x] = 0
    # set pointer from starting point
    curr_y = start_y
    curr_x = start_x
    potential_next = [(curr_y, curr_x - 1), (curr_y, curr_x + 1), (curr_y - 1, curr_x), (curr_y + 1, curr_x)]

    while not all(garden[y][x] == 0 for y, x in potential_next):

        current_max = [(0, 0), 0]

        for y, x in potential_next:
            if garden[y][x] > current_max[1]:
                current_max = [(y, x), garden[y][x]]

        # add next biggest value to counter
        counter += current_max[1]
        # set value to 0 as mark of eaten
        garden[current_max[0][0], current_max[0][1]] = 0
        # move pointer to next square
        curr_x, curr_y = current_max[0][1], current_max[0][0]

    return counter
