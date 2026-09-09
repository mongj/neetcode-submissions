class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        nr = len(grid)
        nc = len(grid[0])

        DIRS = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= nr or c >= nc:
                return
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in DIRS:
                dfs(r+dr, c+dc)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        
        return count