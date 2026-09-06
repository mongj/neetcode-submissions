class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
        nr = len(board)
        nc = len(board[0])

        def existsFrom(r: int, c: int, n: int) -> bool:
            if n == len(word):
                return True
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return False
            if board[r][c] != word[n]:
                return False

            # mark current cell as visited
            original_value = board[r][c]
            board[r][c] = "."
            
            # 4 cases: recurse in each direction
            for dr, dc in DIRS:
                if existsFrom(r + dr, c + dc, n + 1):
                    return True
            
            # reset the board
            board[r][c] = original_value
            
            return False

        
        for r in range(nr):
            for c in range(nc):
                if existsFrom(r, c, 0):
                    return True

        return False