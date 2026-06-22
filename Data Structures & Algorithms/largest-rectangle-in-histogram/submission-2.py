class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        stack = []
        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            # now the top of the stack is the first element shorter than i
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        largestSeen = 0
        for i, height in enumerate(heights):
            currArea = height * (rightMost[i] - leftMost[i] - 1)
            largestSeen = max(largestSeen, currArea)

        return largestSeen