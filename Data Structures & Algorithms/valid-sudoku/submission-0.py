class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for row in board:
            seen = set()
            for cell in row:
                if cell != ".":
                    if cell in seen:
                        return False
                    else:
                        seen.add(cell)
        # check each column
        row_count = len(board)
        col_count = len(board[0])
        for c in range(col_count):
            seen = set()
            for r in range(row_count):
                if board[r][c] != ".":
                    if board[r][c] in seen:
                        return False
                    else:
                        seen.add(board[r][c])
        # check each 3x3 square
        for i in range(3):
            for j in range(3):
                top_left = (i * 3, j * 3)
                seen = set()
                for r in range(top_left[0], top_left[0] + 3):
                    for c in range(top_left[1], top_left[1] + 3):
                        if board[r][c] != ".":
                            if board[r][c] in seen:
                                return False
                            else:
                                seen.add(board[r][c])
        return True
