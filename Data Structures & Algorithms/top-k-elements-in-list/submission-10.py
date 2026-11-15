from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        freqToNumsMap = [[] for _ in range(len(nums))]
        for num, count in count.items():
            freqToNumsMap[count-1].append(num)
        
        out = []
        for i in range(len(nums)-1, -1, -1):
            if freqToNumsMap[i]:
                for num in freqToNumsMap[i]:
                    out.append(num)
                    k -= 1
                    if k == 0:
                        return out