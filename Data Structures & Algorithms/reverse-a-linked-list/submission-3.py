# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            l = head
            c = l.next
            r = c.next
            head.next = None

            while c is not None:
                c.next = l
                l = c
                c = r
                r = r.next if r is not None else None
            head = l
            return head