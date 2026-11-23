class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetCount = 0
        n = len(position)

        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))
        cars.sort()

        remainingTime = 0
        for i in range(n - 1, -1, -1):
            currRemainingTime = (target - cars[i][0]) / cars[i][1]
            if currRemainingTime > remainingTime:
                remainingTime = currRemainingTime
                fleetCount += 1

        return fleetCount