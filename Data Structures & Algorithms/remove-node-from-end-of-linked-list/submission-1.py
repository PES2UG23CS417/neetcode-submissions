# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        length = 0
        while (ptr is not None):
            length += 1
            ptr = ptr.next
        print(length) # 3 therefore 3-2+1 is required
        ptr = head
        i = 0
        if head is None:
            return head
        elif n == length:
            temp = head
            head = head.next
            temp = None
            return head
        else:
            while (i != (length - n)):
                i += 1
                prev = ptr
                ptr = ptr.next
            prev.next = ptr.next
            ptr.next = None
            return head
