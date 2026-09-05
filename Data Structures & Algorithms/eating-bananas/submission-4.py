class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            hoursNeeded = 0
            for pile in piles:
                hoursNeeded += math.ceil(pile / k)
            return hoursNeeded <= h

        minK, maxK = 1, max(piles)
        while minK < maxK:
            midK = minK + (maxK - minK) // 2
            if canFinish(midK):
                maxK = midK
            else:
                minK = midK + 1
        return minK