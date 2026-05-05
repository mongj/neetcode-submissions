class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, num in enumerate(nums):
            index[num] = i
        for i, num in enumerate(nums):
            if (target - num) in index and i != index[target - num]:
                return [i, index[target - num]]
