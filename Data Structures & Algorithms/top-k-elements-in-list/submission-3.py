class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        sorted_freq = list(sorted(freq.items(), key=lambda x: x[1], reverse=True))[:k]
        print(sorted_freq)
        topK = list(map(lambda x: x[0], sorted_freq))
        return topK