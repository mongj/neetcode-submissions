class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        for i in range(1, len(height) - 1):
            # find largest element to the left and right of i
            l = max(height[:i])
            r = max(height[i+1:])
            if l > height[i] and r > height[i]:
                res += (min(l, r) - height[i])

        # stack = []
        # for i in range(len(height)):
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