class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if m > 0 and m < len(nums) - 1 and nums[m] < nums[m-1] and nums[m] < nums[m+1]:
                return nums[m]
            elif nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m - 1
        return nums[l]