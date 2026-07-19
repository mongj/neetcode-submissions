class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            # the array is split into at most 2 monotonically inreasing subarrays
            #   -> 1 array if rotated exactly n times, 2 subarrays otherwise
            # we observe that:
            # 1) the last element is always part of the smaller subarray
            # 2) the last element in the smaller subarray is still SMALLER than any element in the larger subarray.
            # We can use this observation to determine whether the mid element falls in the smaller or larger subarray
            if nums[mid] > nums[-1]:
                # we're in the larger subarray, search on the right
                l = mid + 1
            else:
                # we're already in the subarray containing the min element, so we continue searching on the left
                r = mid

        return nums[l]