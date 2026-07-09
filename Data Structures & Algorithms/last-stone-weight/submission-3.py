class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for s in stones:
            heapq.heappush(heap, -s)
        
        lastStoneWeight = 0
        
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, -abs(x - y))
            

        return -heap[0] if len(heap) == 1 else 0