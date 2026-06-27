class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) == 0 or target < 0:
            return []
        if target == 0:
            return [[]]

        # at each step, we can either use the number or skip it and never use it again
        # option 1: use the number and keep it for next time
        sub1 = [[nums[0]] + s for s in self.combinationSum(nums, target - nums[0])]
        # option 2: skip the number and never use it again
        sub2 = self.combinationSum(nums[1:], target)

        return sub1 + sub2