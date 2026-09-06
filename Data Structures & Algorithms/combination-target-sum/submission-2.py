class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or target < 0:
            return []
        if target == 0:
            return [[]]

        # case 1: use nums[0]
        sub1 = [[nums[0]] + s for s in self.combinationSum(nums, target - nums[0])]
        # case 2: don't use nums[0]
        sub2 = self.combinationSum(nums[1:], target)

        return sub1 + sub2
