class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1-pass solution
        #
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [[set() for i in range(3)] for i in range(3)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]

                if cell == ".":
                    continue

                if cell in rows[r] or cell in cols[c] or cell in boxes[r//3][c//3]:
                    return False
                
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[r//3][c//3].add(cell)
        
        return True

        # 3-pass solution
        #
        # # check duplicates in every row
        # for row in range(9):
        #     seen = set()
        #     for col in range(9):
        #         if board[row][col] in seen:
        #             return False
        #         elif board[row][col] != ".":
        #             seen.add(board[row][col])
        
        # # check duplicates in every col
        # for col in range(9):
        #     seen = set()
        #     for row in range(9):
        #         if board[row][col] in seen:
        #             return False
        #         elif board[row][col] != ".":
        #             seen.add(board[row][col])
        
        # # check duplicates in every sub-box
        # for start_row in range(0, 9, 3):
        #     for start_col in range(0, 9, 3):
        #         seen = set()
        #         for row in range(start_row, start_row + 3):
        #             for col in range(start_col, start_col + 3):
        #                 if board[row][col] in seen:
        #                     return False
        #                 elif board[row][col] != ".":
        #                     seen.add(board[row][col])

        
        # return True