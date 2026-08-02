# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        if head is None:
            return False
        else:
            ptr = head
            while ptr is not None:
                if ptr in visited:
                    return True
                else:
                    visited.add(ptr)
                    ptr = ptr.next
        return False