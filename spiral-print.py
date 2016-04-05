"""Print matrix in spiral order, starting from the center."""


def spiral(n):
    """Populate n x n 2D array with number 0-9 in spiral order"""

    # construct 2D array with 0s
    array = [[0 for i in range(n)] for i in range(n)]

    # determine center point
    curr_y, curr_x = n / 2, (n - 1) / 2

    # directions sequence: up, right, down, left
    directions = [(-1, 0),  (0, 1), (1, 0), (0, -1)]

    max_steps = 1
    steps = 0
    curr_direction = 0

    for i in range(1, (n**2 + 1)):

        array[curr_y][curr_x] = i % 10

        steps += 1

        curr_x = directions[curr_direction][1] + curr_x
        curr_y = directions[curr_direction][0] + curr_y

        if steps == max_steps:
            curr_direction = (curr_direction + 1) % 4
            if curr_direction in [0, 2]:
                max_steps += 1
            steps = 0

    return array


def print_2D_arr(arr):
    """Print 2D arr in pretty way"""

    for i in range(len(arr)):
        print arr[i]


if __name__ == "__main__":
    print_2D_arr(spiral(3))
