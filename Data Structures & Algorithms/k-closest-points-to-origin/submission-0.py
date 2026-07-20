class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distToOrigin(point: List[int]) -> int:
            return math.sqrt(point[0]**2 + point[1]**2)
        
        heap = []
        heapq.heapify(heap)
        for point in points:
            heapq.heappush(heap, (-distToOrigin(point), point))
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [p[1] for p in heap]