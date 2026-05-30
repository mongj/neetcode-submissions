class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))] 
        cars.sort(key=lambda c: c[0], reverse=True)
        # start from the car closest to the end, which is always in its own fleet
        # now iteratively check the car after it, if it can catch up to the last car
        # then they are in the same fleet
        # else start a new fleet
        currentLeader = cars[0]
        bestTimeToTarget = (target - currentLeader[0]) / currentLeader[1]
        fleetCount = 1
        for car in cars[1:]:
            # if car can reach the target before current leader (assuming passing is allowed)
            # then without passing it will still catch up to the leader
            # we can therefore consider the car to be in the same fleet
            carTimeToTarget = (target - car[0]) / car[1]
            if carTimeToTarget > bestTimeToTarget:
                currentLeader = car
                bestTimeToTarget = carTimeToTarget
                fleetCount += 1
        return fleetCount