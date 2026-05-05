class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            # keep appending temps while maintaining
            # a monotonically decreasing stack
            if len(stack) > 0:
                # pop temperatures if needed before appending
                while len(stack) > 0 and t > stack[-1][0]:
                    _, item_idx = stack.pop()
                    output[item_idx] = i - item_idx
            stack.append((t, i))

        return output

# [2, 1, 1, 3]
# [3, 2, 1, 0]