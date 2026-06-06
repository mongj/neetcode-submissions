class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nextZeroIdx = 0
        while nextZeroIdx < n:
            # find the next 0
            while nextZeroIdx < n and nums[nextZeroIdx] != 0:
                nextZeroIdx += 1
            
            if nextZeroIdx == n:
                return
            
            # find the next non-zero
            nextNonZeroIdx = nextZeroIdx + 1
            while nextNonZeroIdx < n and nums[nextNonZeroIdx] == 0:
                nextNonZeroIdx += 1
            
            if nextNonZeroIdx == n:
                return

            # swap
            nums[nextZeroIdx], nums[nextNonZeroIdx] = nums[nextNonZeroIdx], nums[nextZeroIdx]

# 001205
# 100205
# 120005
# 125000