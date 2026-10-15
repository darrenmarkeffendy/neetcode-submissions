# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n):
            first = first.next

        while first.next:
            first = first.next
            second = second.next

        next_node = second.next.next
        second.next = next_node

        return dummy.next

        