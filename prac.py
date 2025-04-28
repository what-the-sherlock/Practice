def is_safe(row, col, board, n):
    # Check this column on the upper side
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens_util(board, row, n, solutions):
    if row == n:
        # Found a valid solution, save it
        solution = []
        for i in range(n):
            line = ''
            for j in range(n):
                if board[i][j] == 1:
                    line += 'Q'
                else:
                    line += '.'
            solution.append(line)
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = 1  # Place queen
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# Example: Solve for 4-Queens
n = 4
all_solutions = solve_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(all_solutions)}\n")
for sol in all_solutions:
    for row in sol:
        print(row)
    print()