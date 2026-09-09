class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nr = len(grid)
        nc = len(grid[0])

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque([])
        visited = set()

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        curr_dist = 0
        while queue:
            # pop all from the current layer
            for _ in range(len(queue)):
                ri, ci = queue.popleft()
                if ri < 0 or ci < 0 or ri >= nr or ci >= nc:
                    continue
                
                if grid[ri][ci] < 0:
                    continue

                if grid[ri][ci] == 0 and curr_dist > 0:
                    continue

                if (ri, ci) in visited:
                    continue

                visited.add((ri, ci))
                grid[ri][ci] = min(grid[ri][ci], curr_dist)

                for dr, dc in dirs:
                    queue.append((ri+dr, ci+dc))
            
            curr_dist += 1


