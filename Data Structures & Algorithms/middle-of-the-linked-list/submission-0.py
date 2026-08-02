# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if head.next is None:
            return head
        
        count = 0
        while node:
            count += 1
            node = node.next
        node = head
        for i in range(count//2):
            node = node.next
        
        return node