class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nr, nc = len(board), len(board[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r: int, c: int) -> None:
            if not (0 <= r < nr and 0 <= c < nc):
                return
            if board[r][c] != "O":
                return
            
            # taint the cell
            board[r][c] = "T"

            # recurse in 4 directions
            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        for r in range(nr):
            dfs(r, 0)
            dfs(r, nc-1)

        for c in range(nc):
            dfs(0, c)
            dfs(nr-1, c)
        
        for r in range(nr):
            for c in range(nc):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"