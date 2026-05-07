class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        boats = 0
        while l <= r:
            # spawn a new boat for the right person
            # try to fit the left person if possible
            boats += 1
            if limit - people[r] >= people[l]:
                l += 1
            r -= 1
        return boats
