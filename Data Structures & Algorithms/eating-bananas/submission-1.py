class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            min_hours = 0
            for pile in piles:
                min_hours += math.ceil(pile / k)
            return min_hours <= h
        
        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            if canFinish(mid):
                # try lower half
                r = mid
            else:
                # try upper half
                l = mid + 1
        # l = r
        return l