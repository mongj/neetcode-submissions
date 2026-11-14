class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numberToIndexMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numberToIndexMap:
                return [numberToIndexMap[complement], i]
            numberToIndexMap[num] = i

