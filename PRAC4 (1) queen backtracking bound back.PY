# implement a solution for a constraint satisfaction problem using backtracking for n-queens problem

def is_safe(row, col, board, n):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True
def solve_n_queens_util(row, board, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(row, col, board, n):
            board[row] = col
            solve_n_queens_util(row + 1, board, n, solutions)
            board[row] = -1  

def solve_n_queens(n):
    board = [-1] * n 
    solutions = []
    solve_n_queens_util(0, board, n, solutions)
    return solutions
def print_solutions(solutions):
    for sol_num, solution in enumerate(solutions, start=1):
        print(f"Solution {sol_num}:")
        for row in solution:
            line = ['.'] * len(solution)
            line[row] = 'Q'
            print(' '.join(line))
        print()
if __name__ == "__main__":
    N = 8
    solutions = solve_n_queens(N)
    print(f"Total solutions for {N}-Queens: {len(solutions)}")
    print_solutions(solutions[:3])