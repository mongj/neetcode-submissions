class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid] and target <= nums[r] and nums[mid] <= nums[-1]:
                l = mid + 1
            elif (target > nums[mid] or target <= nums[r]) and nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
