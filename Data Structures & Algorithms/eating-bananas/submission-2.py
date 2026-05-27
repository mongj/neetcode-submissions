class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursNeededToFinish(k: int) -> int:
            h = 0
            for pile in piles:
                h += math.ceil(pile / k)
            return h
        
        l = 1
        r = max(piles)
        minK = r
        while l <= r:
            k = l + (r - l) // 2
            # test if koko can finish eating bananas in h hours
            # at a rate of k bananas per hour
            hoursNeeded = hoursNeededToFinish(k)
            if hoursNeeded <= h:
                # can finish
                minK = min(minK, k)
                r = k - 1
            else:
                # can't finish in time, try to eat more per hour
                l = k + 1
        return minK
