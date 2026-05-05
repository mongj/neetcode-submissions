class Solution:
    def maxArea(self, heights: List[int]) -> int:
        curr = 0
        acc = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            curr = (r - l) * min(heights[l], heights[r])
            acc = max(acc, curr)
            # move the smaller bar to the next largest position
            if heights[l] < heights[r]:
                while heights[l + 1] <= heights[l] and l < r:
                    l += 1
                l += 1
            else:
                while heights[r - 1] <= heights[r] and r > l:
                    r -= 1
                r -= 1

        return acc