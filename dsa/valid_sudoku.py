"""Given a 9x9 Sudoku board, determine if it's valid according to these rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes must contain the digits 1-9 without repetition.
Note: only the filled cells need to be validated according to these rules — empty cells are represented by '.' and can be ignored. The board doesn't need to be solvable, just currently valid."""


class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if value in rows[r] or value in cols[c] or value in boxes[box_index]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)

        return True


solution = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"],
]
print(solution.isValidSudoku(board))
