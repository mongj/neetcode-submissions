class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        def findPivot(l: int, r: int) -> int:
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    # we found the smallest element in nums
                    return mid
                elif nums[r] < nums[mid]:
                    # search in upper half
                    l = mid + 1
                else:
                    # search in lower half
                    r = mid - 1
            return l

        # find pivot
        l = 0
        r = len(nums) - 1
        pivot = findPivot(l, r)
        print(pivot)
        
        def search(l: int, r: int) -> int:
            print(f"searching from #{l} -> #{r}")
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    # search in lower half
                    r = mid - 1
                else:
                    # search in upper half
                    l = mid + 1
            return -1

        # decide which half to seach from
        if target >= nums[pivot] and target <= nums[r]:
            return search(pivot, r)
        return search(l, pivot - 1)
