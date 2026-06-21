import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        return -heapq.nsmallest(self.k, self.heap)[-1]
