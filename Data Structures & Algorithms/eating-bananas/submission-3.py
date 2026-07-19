class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            hoursNeeded = sum([math.ceil(numBananas / k) for numBananas in piles])
            return hoursNeeded <= h
        
        low, high = 1, max(piles)

        while low < high:
            mid = low + (high - low) // 2
            if canFinish(mid):
                high = mid
            else:
                low = mid + 1
        return low
