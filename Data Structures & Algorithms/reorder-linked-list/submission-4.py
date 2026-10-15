# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head

        while l2 and l2.next:
            l2 = l2.next.next
            l1 = l1.next
    
        second_half = l1.next
        l1.next = None
        first_half = head

        current = second_half
        previous = None
        save_next = None

        while current:
            save_next = current.next
            current.next = previous
            previous = current
            current = save_next

        second_half = previous

        dummy = ListNode()
        returned = dummy
        count = 0

        while first_half and second_half:
            if count % 2:
                returned.next = second_half
                second_half = second_half.next
            else:
                returned.next = first_half
                first_half = first_half.next   
            count += 1
            returned = returned.next


        if first_half:
            returned.next = first_half
        elif second_half:
            returned.next = second_half




