class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        index = {}
        for ck, cv in counter.items():
            if cv in index:
                index[cv].append(ck)
            else:
                index[cv] = [ck]
        remaining = k
        i = len(nums)
        out = []
        while remaining > 0 and i > 0:
            if i in index:
                out.extend(index[i])
                remaining -= len(index[i])
            i -= 1
        return out