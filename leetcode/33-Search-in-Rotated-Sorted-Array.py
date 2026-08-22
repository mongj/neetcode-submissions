class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif (nums[mid] > nums[0] and nums[0] <= target < nums[mid]) or (nums[mid] < nums[0] and (target < nums[mid] or target >= nums[0])):
                r = mid - 1
            else:
                l = mid + 1
        return -1