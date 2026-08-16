class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        cache = {}
        def sub(n: int) -> int:
            if n <= 0:
                return 0
            if n not in cache:
                cache[n] = min(
                    (sub(n - 1) + costs[n-1] + 1),
                    (sub(n - 2) + costs[n-1] + 4),
                    (sub(n - 3) + costs[n-1] + 9)
                )
            return cache[n]
        return sub(n)