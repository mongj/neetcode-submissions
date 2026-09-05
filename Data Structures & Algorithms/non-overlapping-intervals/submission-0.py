class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        lastInterval = intervals[0]
        countToDelete = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastInterval[1]:
                # delete the one with the later end time
                countToDelete += 1
                if intervals[i][1] < lastInterval[1]:
                    lastInterval = intervals[i]
            else:
                lastInterval = intervals[i]
        return countToDelete