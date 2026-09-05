class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def isPeak(i: int) -> bool:
            if i == 0:
                return nums[i+1] < nums[i]
            if i == len(nums) - 1:
                return nums[i-1] < nums[i]
            return nums[i-1] < nums[i] and nums[i+1] < nums[i]
            
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l) // 2
            if isPeak(m):
                return m
            # if m is not a peak, then at least one of
            # (m+1 or m-1) must be strictly larger than m
            if nums[m+1] > nums[m]:
                l = m+1
            else:
                r = m-1
        return l