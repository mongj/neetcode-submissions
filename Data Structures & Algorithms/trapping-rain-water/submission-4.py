class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        tallestToLeft = [0] * n
        tallestToRight = [0] * n
        for i in range(1, n):
            tallestToLeft[i] = max(tallestToLeft[i-1], height[i-1])
        for i in range(n-2, -1, -1):
            tallestToRight[i] = max(tallestToRight[i+1], height[i+1])
        
        total_area = 0
        for i in range(1, n-1):
            total_area += max(min(tallestToLeft[i], tallestToRight[i]) - height[i], 0)
        return total_area