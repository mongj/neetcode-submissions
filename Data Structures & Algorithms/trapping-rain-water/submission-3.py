class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0
        width = len(height)
        
        for i in range(width - 1):
            if height[i] > height[i + 1]:
                l = i
                r = i + 1
                minHeight = height[i + 1]
                # keep expanding right pointer until the end is reached or
                # we reach the right bound:
                # 1) greater or equal height as l, OR
                # 2) lower than l, but it's the peak (next element is lower)
                while r < width:
                    # keep expanding right pointer until it's greater than
                    # minHeight or the end is reached
                    while r < width and height[r] <= minHeight:
                        r += 1
                    if r >= width:
                        break
                    maxArea += (r - l - 1) * (min(height[l], height[r]) - minHeight)
                    minHeight = min(height[l], height[r])
                    if height[r] >= height[l]:
                        break
                    
        return maxArea