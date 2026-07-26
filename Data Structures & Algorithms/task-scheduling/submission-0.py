class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            i = ord(task) - ord('A')
            freq[i] = freq.get(i, 0) + 1
        
        heap = []
        heapq.heapify(heap)

        for (i, count) in freq.items():
            heapq.heappush(heap, (-count, i, 0))

        # keep a running count of the cycle count after each task
        cycles = 0

        queue = deque()

        while heap or queue:
            while queue and queue[0][2] <= cycles:
                task = queue.popleft()
                heapq.heappush(heap, task)

            if heap:
                task = heapq.heappop(heap)
                count, i, nextTime = -task[0], task[1], task[2]
                print(count, chr(i + ord('A')), nextTime)

                # cycle count after the task is completed
                cycles += 1

                remainingTasks = count - 1
                if remainingTasks > 0:
                    queue.append((-remainingTasks, i, cycles + n))
            else:
                # we reach here when there's nothing in the queue ready to be run
                # and the heap is still empty. So the processor has to be idle until
                # the next available task
                cycles = queue[0][2]


        return cycles