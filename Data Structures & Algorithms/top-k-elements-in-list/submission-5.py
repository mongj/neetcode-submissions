class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        for n, f in freq.items():
            buckets[f].append(n)

        topK = []
        for i in range(len(nums), -1, -1):
            if buckets[i]:
                for n in buckets[i]:
                    if k > 0:
                        topK.append(n)
                        k = k - 1
        return topK