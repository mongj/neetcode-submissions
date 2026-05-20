from functools import cmp_to_key

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        def compare(a: int, b: int) -> int:
            if freq[a] < freq[b]:
                return -1
            if freq[a] == freq[b]:
                return b - a
            return 1
        nums.sort(key=cmp_to_key(compare))
        return nums