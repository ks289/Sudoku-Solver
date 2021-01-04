"""
This will find the next empty tile on the board.
Returns:
    This will return either a (row, col) tuple of the empty tile or
    (None, None) tuple if the board is full.
"""
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

"""
This will return if the guess (the number to place in an empty tile) is
valid or not. This considers the rules of sudoku: no other occurrences of the 
number within the row, column and 3x3 matrix.
"""
def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True

"""
This is the main loop which will solve the sudoku puzzle by attempting every possible
combination at a given empty tile on the board, and backtracking if required to try
another combination until the board is either solved or shown to be impossible.
"""
def solve_sudoku(puzzle):
    # Make a random guess initially.
    row, col = find_next_empty(puzzle)
    
    # Base case of the recursion, solved puzzle.
    if row is None:
        return True
    
    # Make a guess with each number at the given empty tile.
    for guess in range(1, 10):
        # If is valid then insert the guess and recurse.
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        # If invalid then reset the tile to be empty and try with a different guess.
        puzzle[row][col] = -1 # reseting the guess
    
    # Attempted every combination so puzzle must be insolvable.
    return False

if __name__ == '__main__':
    # Example invalid board.
    example_board = [
        [3,9,-1,-1,5,-1,-1,-1,-1],
        [-1,-1,-1,2,-1,-1,-1,-1,5],
        [-1,-1,-1,7,1,9,-1,8,-1],
        [-1,5,-1,-1,6,8,-1,-1,-1],
        [2,-1,6,-1,-1,3,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1,4],
        [5,-1,-1,-1,-1,-1,-1,-1,-1],
        [6,7,-1,1,-1,5,-1,4,-1],
        [1,-1,9,-1,-1,-1,2,-1,-1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
    
    # Example invalid board.
    example_board2 = [
        [8,3,-1,-1,7,-1,-1,-1,-1],
        [6,-1,-1,1,9,5,-1,-1,-1],
        [-1,9,8,-1,-1,-1,-1,6,-1],
        [8,-1,-1,-1,6,-1,-1,-1,3],
        [4,-1,-1,8,-1,3,-1,-1,1],
        [7,-1,-1,-1,2,-1,-1,-1,6],
        [-1,6,-1,-1,-1,-1,2,8,-1],
        [-1,-1,-1,4,1,9,-1,-1,5],
        [-1,-1,-1,-1,8,-1,-1,7,9]
    ]
    print(solve_sudoku(example_board2))
    print(example_board2)
    