# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        heap = []
        tail = dummy
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            value, index, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, index, node))
        
        return dummy.next
