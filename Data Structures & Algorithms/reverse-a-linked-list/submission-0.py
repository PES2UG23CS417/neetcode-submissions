# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            l = head
            prev = head.next
            r = prev.next
            head.next = None

            while prev is not None:
                prev.next = l
                l = prev
                prev = r
                r = r.next if r is not None else None

            return l