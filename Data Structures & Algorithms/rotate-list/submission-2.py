# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        count = 0
        tail = head
        while tail.next:
            tail = tail.next
            count += 1
        
        count += 1
        k = k % count
        if k == 0:
            return head
        
        cur = head
        for i in range(count - k - 1):
            cur = cur.next
        
        tail.next = head
        head = cur.next
        cur.next = None
        return head