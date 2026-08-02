# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        left = head
        curr = head.next
        right = curr.next
        head.next = None
        while curr:
            curr.next = left
            left = curr
            curr = right
            right = right.next if right else None
        
        head = left
        return head