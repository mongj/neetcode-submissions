class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largestSeen = 0
        for i, height in enumerate(heights):
            l = r = i
            while l >= 0 and heights[l] >= height:
                l -= 1
            while r < len(heights) and heights[r] >= height:
                r += 1
            currArea = height * (r - l - 1)
            largestSeen = max(largestSeen, currArea)
        return largestSeen