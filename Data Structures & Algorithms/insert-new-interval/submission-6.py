class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        inserted = False
        i = 0

        while i < len(intervals):
            # 1. pick an interval to insert
            if not inserted and newInterval[0] < intervals[i][0]:
                insertionInterval = newInterval
                inserted = True
            else:
                insertionInterval = intervals[i]
                i += 1
                
            # 2. insert the interval
            if len(out) == 0 or insertionInterval[0] > out[-1][1]:
                out.append(insertionInterval)
            else:
                out[-1][1] = max(out[-1][1], insertionInterval[1])

        if not inserted:
            if len(out) == 0 or newInterval[0] > out[-1][1]:
                out.append(newInterval)
            else:
                out[-1][1] = max(out[-1][1], newInterval[1])

        return out