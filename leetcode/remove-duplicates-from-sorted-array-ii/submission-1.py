class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i > 1 and nums[i] == nums[k - 1] == nums[k - 2]:
                continue
            nums[k] = nums[i]
            k += 1
        return k

        