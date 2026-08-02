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
        node = left.next
        right = node.next

        head.next = None
        while right:
            node.next = left
            left = node
            node = right
            right = right.next

        node.next = left
        head = node

        return head