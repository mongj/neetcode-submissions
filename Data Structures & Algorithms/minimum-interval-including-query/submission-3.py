class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        def containsQuery(i: int, q: int) -> bool:
            return intervals[i][0] <= q and intervals[i][1] >= q

        intervals.sort(key=lambda x: x[0])
        res = [0] * len(queries)
        heap = []
        i = 0
        for origIndex, q in sorted(enumerate(queries), key=lambda x: x[1]):
            print(origIndex, q)
            while i < len(intervals) and intervals[i][0] <= q:
                if containsQuery(i, q):
                    heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1], intervals[i]))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            minSize = heap[0][0] if heap else -1
            res[origIndex] = minSize
        return res