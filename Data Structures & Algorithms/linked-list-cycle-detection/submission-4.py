# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # s, f = head, head

        # while f and f.next:
        #     s = s.next
        #     f = f.next.next
        #     if s == f:
        #         return True
        # return False
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        return False