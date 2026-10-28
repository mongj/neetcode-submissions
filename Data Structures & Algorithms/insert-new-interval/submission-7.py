class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        hasInserted = False
        i = 0

        intervals.sort()

        while i < len(intervals) or not hasInserted:
            if not hasInserted and (i >= len(intervals) or intervals[i][0] > newInterval[0]):
                intervalToInsert = newInterval
                hasInserted = True
            else:
                intervalToInsert = intervals[i]
                i += 1

            if len(out) == 0 or out[-1][1] < intervalToInsert[0]:
                out.append(intervalToInsert)
            else:
                out[-1][1] = max(out[-1][1], intervalToInsert[1])

        return out