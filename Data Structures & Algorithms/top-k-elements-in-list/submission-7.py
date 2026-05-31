class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums))]
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        for n, f in freqMap.items():
            freq[f - 1].append(n)
        out = []
        for numArr in freq[::-1]:
            for num in numArr:
                if k > 0:
                    out.append(num)
                    k -= 1
                else:
                    break
        return out