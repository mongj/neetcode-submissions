class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []
        for i in range(len(intervals)):
            if len(out) == 0 or intervals[i][0] > out[-1][1]:
                out.append(intervals[i])
            else:
                out[-1][1] = max(out[-1][1], intervals[i][1])
        return out