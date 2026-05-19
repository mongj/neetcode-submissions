class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        res = []
        for k, v in freq.items():
            if v > n // 3:
                res.append(k)
        return res