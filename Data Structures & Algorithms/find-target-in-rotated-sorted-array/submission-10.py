class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[-1]:
                # we're in the left subarray (before pivot)
                if target >= nums[0] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # we're in the right subarray (after pivot)
                if target > nums[mid] and target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
