class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumMap = { 0: 1 }
        acc = 0
        count = 0
        for num in nums:
            acc += num
            if acc - k in prefixSumMap:
                count += prefixSumMap[acc - k]
            prefixSumMap[acc] = prefixSumMap.get(acc, 0) + 1
        return count