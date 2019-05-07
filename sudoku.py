import random


def generate_possible_matrix():
    puzzle = [
        [0, 0, 0, 2, 1, 4, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 9],
        [0, 6, 4, 0, 0, 0, 5, 2, 0],
        [0, 9, 0, 3, 0, 7, 0, 6, 0],
        [0, 0, 6, 0, 0, 0, 4, 0, 0],
        [0, 8, 0, 0, 6, 0, 0, 9, 0],
        [5, 1, 0, 0, 2, 0, 0, 8, 3],
        [8, 0, 0, 0, 3, 0, 0, 0, 4],
        [0, 0, 0, 7, 0, 8, 0, 0, 0]
    ]

    for i in range(9):
        pre_list = [num for num in range(1, 10)]
        random.shuffle(pre_list)

        for number in puzzle[i]:
            if number != 0:
                pre_list.remove(number)

        for j in range(9):
            if puzzle[i][j] == 0:
                puzzle[i][j] = pre_list.pop()
    return puzzle


def check_puzzle(matrix):
    # check if every column has repeat number
    for row in range(9):
        column = [matrix[col][row] for col in range(9)]
        if len(set(column)) < 9:
            return False
    return True


while True:
    new_sudoku = generate_possible_matrix()
    for rows in new_sudoku:
        print(rows)
    print('*' * 27)
    if check_puzzle(new_sudoku):
        break
print()
