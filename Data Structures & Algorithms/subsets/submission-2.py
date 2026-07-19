import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        curr = nums[0]
        sub = self.subsets(nums[1:])

        # for every subset in sub, we can either add curr or not
        return sub + [arr + [curr] for arr in sub]