class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canFinish(shipCapacity: int, targetDays: int) -> bool:
            daysTaken = 0
            currLoad = 0
            for weight in weights:
                if currLoad + weight <= shipCapacity:
                    currLoad += weight
                else:
                    daysTaken += 1
                    currLoad = weight
            if currLoad > 0:
                daysTaken += 1
            
            return daysTaken <= targetDays

        lowerBoundCap = max(weights)
        upperBoundCap = sum(weights)
        while lowerBoundCap < upperBoundCap:
            cap = lowerBoundCap + (upperBoundCap - lowerBoundCap) // 2
            # check if can finish within specified days
            if canFinish(cap, days):
                upperBoundCap = cap
            else:
                lowerBoundCap = cap + 1
        
        return lowerBoundCap

        