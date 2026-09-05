class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            
            # 2 cases to handle
            if nums[-1] > nums[mid]:
                # pivot is on the left
                if target > nums[mid] and target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # pivot is on the right
                if target >= nums[0] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
