class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for curr_idx, curr_temp in enumerate(temperatures):
            while len(stack) > 0 and curr_temp > stack[-1][0]:
                _, prev_idx = stack.pop()
                out[prev_idx] = curr_idx - prev_idx
            stack.append((curr_temp, curr_idx))
        return out
