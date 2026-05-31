class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        items = sorted(freq.items(), key=lambda i: i[1], reverse=True)
        return list(map(lambda i: i[0], items[:k]))