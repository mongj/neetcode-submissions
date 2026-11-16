class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, curr_area)
            if heights[l] < heights[r]:
                # l is limiting, so we move l inwards
                l += 1
            else:
                r -= 1
        return max_area