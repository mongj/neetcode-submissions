class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:
                # pivot is on the right
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                # pivot is on the left
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        return False