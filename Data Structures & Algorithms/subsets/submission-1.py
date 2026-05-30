import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        sub = self.subsets(nums[:-1])
        sub2 = copy.deepcopy(sub)
        for arr in sub:
            arr.append(nums[-1])
        sub.extend(sub2)
        return sub