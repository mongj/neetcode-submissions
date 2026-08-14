class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = []
        cols = []

        for i in range(n):
            rows.append(tuple(grid[i])) # row[i]
            cols.append(tuple([grid[r][i] for r in range(n)])) # col[i]

        count = 0
        for row in rows:
            for col in cols:
                if row == col:
                    count += 1
                
        return count
