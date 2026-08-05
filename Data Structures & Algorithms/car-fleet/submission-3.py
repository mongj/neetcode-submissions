class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))] 
        cars.sort(key=lambda c: c[0], reverse=True)
        # start from the car closest to the end, which is always in its own fleet
        # now iteratively check the car after it, if it can catch up to the last car
        # then they are in the same fleet
        # else start a new fleet
        numFleets = 1
        currFleetArrivalTime = (target - cars[0][0]) / cars[0][1]
        for car in cars:
            timeToReach = (target - car[0]) / car[1]
            if timeToReach > currFleetArrivalTime:
                # new fleet
                numFleets += 1
                currFleetArrivalTime = timeToReach
        return numFleets