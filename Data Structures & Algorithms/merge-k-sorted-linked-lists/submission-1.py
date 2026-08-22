# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode()
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))
        
        while len(heap) > 0:
            _, i, smallestNode = heapq.heappop(heap)
            head.next = smallestNode
            head = head.next
            if smallestNode.next:
                heapq.heappush(heap, (smallestNode.next.val, i, smallestNode.next))

        return dummy.next