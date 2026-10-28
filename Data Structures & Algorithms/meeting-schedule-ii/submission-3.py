"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        roomsNeeded = 0
        rooms = []
        heapq.heapify(rooms)

        for interval in intervals:
            # evict all the empty rooms
            while rooms and rooms[0] <= interval.start:
                heapq.heappop(rooms)

            # occupy a new room
            heapq.heappush(rooms, interval.end)

            # update roomsNeeded
            roomsNeeded = max(roomsNeeded, len(rooms))

        return roomsNeeded