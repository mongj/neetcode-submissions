class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def shouldAdd(i: int, k: int) -> bool:
            if i == 0 or i == 1 or nums[i] != nums[k-1]:
                return True
            else:
                return nums[i] != nums[k-2]
            
        k = 0
        for i in range(len(nums)):
            if shouldAdd(i, k):
                nums[k] = nums[i]
                k += 1
        return k

        