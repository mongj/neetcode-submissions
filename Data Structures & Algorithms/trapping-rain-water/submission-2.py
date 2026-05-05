class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)

        # for i in range(1, n - 1):
        #     # find largest element to the left and right of i
        #     l = max(height[:i])
        #     r = max(height[i+1:])
        #     if l > height[i] and r > height[i]:
        #         res += (min(l, r) - height[i])

        # prefix[i] is the max height to the left of i
        prefix = [0] * n
        # suffix[i] is the max height to the right of i
        suffix = [0] * n

        for i in range(1, n - 1):
            prefix[i] = max(prefix[i - 1], height[i - 1])
            suffix[n - 1 - i] = max(suffix[n - i], height[n - i])

        for i in range(1, n - 1):
            if prefix[i] > height[i] and suffix[i] > height[i]:
                res += (min(prefix[i], suffix[i]) - height[i])

        # stack = []
        # for i in range(n):
        #     if len(stack) == 0:
        #         stack.append(height[i])
        #     elif height[i] <= stack[-1]:
        #         stack.append(height[i])
        #     elif height[i] > stack[-1]:
        #         while len(stack) > 0 and height[i] > stack[-1]:
        #             h = stack.pop()
        #             if len(stack) > 0:
        #                 res += (min(height[i], stack[0]) - h)
        #         stack.append(height[i])
        return res