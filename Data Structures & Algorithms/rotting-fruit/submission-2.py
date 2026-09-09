class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        q = deque([])
        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # insert all the rotten fruits into a queue
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 2:
                    q.append((r, c, 0))

        # multi-source bfs from all the rotten fruits
        curr_minute = 0
        while q:
            # pops everything from the current layer
            for _ in range(len(q)):
                r, c, m = q.popleft()
                
                # skip if invalid
                if r < 0 or c < 0 or r >= nr or c >= nc:
                    continue
                if grid[r][c] == 0:
                    continue
                if (r, c) in visited:
                    continue

                visited.add((r, c))
                grid[r][c] = 2
                curr_minute = max(curr_minute, m)

                for dr, dc in directions:
                    q.append((r+dr, c+dc, m+1))

        # check if any fresh fruit is left
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    return -1

        return curr_minute