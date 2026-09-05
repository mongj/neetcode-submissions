"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # rooms is a minheap representing all the currently occupied rooms
        # sorted by the end time
        rooms = []
        heapq.heapify(rooms)
        # maximum number of occupied rooms we have at any point in time
        roomCount = 0

        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals)):
            currMeeting = intervals[i]

            # first eject all the empty rooms
            while len(rooms) > 0 and currMeeting.start >= rooms[0][2].end:
                heapq.heappop(rooms)

            # occupy a room for the current meatting
            heapq.heappush(rooms, (currMeeting.end, i, currMeeting))

            # update roomCount at the end of each iteration
            roomCount = max(roomCount, len(rooms))

        return roomCount