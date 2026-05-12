class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        # keep a monotonically decreasing stack
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                si, _ = stack.pop()
                res[si] = i - si
            stack.append((i, t))
        return res