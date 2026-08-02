# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return []
        
        temp = head
        length = 1

        while temp.next is not None:
            temp = temp.next
            length += 1

        if n == length: # remove the head
            temp = head
            head = head.next
            temp.next = None

        else:
            temp = head
            p = 0
            prev = temp
            while p != (length - n):
                prev = temp
                temp = temp.next
                p += 1

            prev.next = temp.next if temp is not None else None

        return head