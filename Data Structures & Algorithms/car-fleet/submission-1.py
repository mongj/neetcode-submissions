class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True, key=lambda c: (c[0], c[1]))
        print(cars)
        for c in cars:
            t = (target - c[0]) / c[1]
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)