def is_safe(board, row, col):
    for prev_row in range(row):
        placed = board[prev_row]
        if placed == col:  # Same column
            return False
        if abs(prev_row - row) == abs(placed - col):  # Diagonal check
            return False
    return True

def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Undo move (backtrack)
        
        # Increment tracker when a configuration is exhausted or fails
        backtrack_count[0] += 1

    backtrack(0)
    return solutions, backtrack_count[0]

def display_board(solution, n):
    print(' +' + '---+' * n)
    for row in range(n):
        print(' |', end='')
        for col in range(n):
            if solution[row] == col:
                print(' Q |', end='')
            else:
                print(' . |', end='')
        print()
        print(' +' + '---+' * n)

# --- Solve for N=4, 6, and 8 ---
for n in [4, 6, 8]:
    solutions, backtracks = solve_n_queens(n)
    print(f'\n========================================')
    print(f'N={n}: {len(solutions)} solutions found, {backtracks} backtracks executed')
    print(f'========================================')
    
    if n == 4:
        print(f'\nAll visual solutions for {n}-Queens:')
        for i, sol in enumerate(solutions, 1):
            print(f'\nSolution {i}: {sol}')
            display_board(sol, n)
