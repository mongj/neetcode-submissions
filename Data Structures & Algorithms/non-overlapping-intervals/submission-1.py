class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        lastInterval = intervals[0]
        for interval in intervals[1:]:
            # if there's an overlap, keep the one that ends earliest
            if interval[0] < lastInterval[1]:
                if interval[1] < lastInterval[1]:
                    lastInterval = interval
                count += 1
            else:
                lastInterval = interval

        return count