class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check duplicates in every row
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] in seen:
                    return False
                elif board[row][col] != ".":
                    seen.add(board[row][col])
        
        # check duplicates in every col
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] in seen:
                    return False
                elif board[row][col] != ".":
                    seen.add(board[row][col])
        
        # check duplicates in every sub-box
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen = set()
                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        if board[row][col] in seen:
                            return False
                        elif board[row][col] != ".":
                            seen.add(board[row][col])

        
        return True