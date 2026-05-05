class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            rem = target - num
            if rem in d and d[rem] != i:
                return [d[rem], i]
            d[num] = i