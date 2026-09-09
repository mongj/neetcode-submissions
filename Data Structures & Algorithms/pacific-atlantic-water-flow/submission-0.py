class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificReachable = set()
        atlanticReachable = set()
        nr, nc = len(heights), len(heights[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(s: set, r: int, c: int) -> None:
            #print("pacific" if s is pacificReachable else "atlantic",r,c)
            if (r, c) in s:
                return
            s.add((r, c))

            for dr, dc in directions:
                rr, cc = r+dr, c+dc
                # print(f"  {rr, cc}")
                if rr >= 0 and cc >= 0 and rr < nr and cc < nc and heights[rr][cc] >= heights[r][c]:
                    dfs(s, rr, cc)

        for r in range(nr):
            dfs(pacificReachable, r, 0)
            dfs(atlanticReachable, r, nc-1)
        for c in range(nc):
            dfs(pacificReachable, 0, c)
            dfs(atlanticReachable, nr-1, c)

        # print("pacific", pacificReachable)
        # print("atlantic", atlanticReachable)

        return [list(coord) for coord in pacificReachable.intersection(atlanticReachable)]