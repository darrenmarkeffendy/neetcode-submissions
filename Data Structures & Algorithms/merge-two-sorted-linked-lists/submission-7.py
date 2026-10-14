# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l2 = list2
        l1 = list1
        dummy = ListNode()
        tail = dummy
        while l1 != None and l2 != None:
            if l2.val < l1.val:
                tail.next = l2
                tail = l2
                l2 = l2.next
            else:
                tail.next = l1
                tail = l1
                l1 = l1.next
        if l1:
            tail.next  = l1
        if l2:
            tail.next = l2
        return dummy.next

        