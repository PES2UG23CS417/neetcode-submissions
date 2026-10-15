# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left, cur, right = head, head.next, head.next.next
        head.next = None

        while cur.next:
            cur.next = left
            left = cur
            cur = right
            right = right.next
        
        cur.next = left
        head = cur

        return head