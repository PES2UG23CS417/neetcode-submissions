# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 3 pointers - prev, h2, tail
        if not head or not head.next or k == 0:
            return head

        tail = head
        count = 1
        while tail.next:
            count += 1
            tail = tail.next
        
        k = k % count
        if k == 0:
            return head

        i = 0
        h2 = head
        print(count)
        
        
        while i < (count - k):
            prev = h2
            h2 = h2.next
            i += 1
        print(head.val, prev.val, h2.val, tail.val)
        
        tail.next = head
        prev.next = None

        return h2