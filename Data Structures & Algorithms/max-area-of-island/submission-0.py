class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        nr = len(grid)
        nc = len(grid[0])

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= nr or c >= nc:
                return 0
            if grid[r][c] == 0:
                return 0

            # set visited nodes to 0 to prevent revisits
            grid[r][c] = 0

            area = 1
            for dr, dc in dirs:
                area += dfs(r+dr, c+dc)

            return area

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    # run dfs to get the size of this island
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea