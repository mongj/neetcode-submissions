class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            if len(res) == 0 or interval[0] > res[-1][1]:
                res.append(interval)
            elif interval[1] > res[-1][1]:
                res[-1][1] = interval[1]
        return res