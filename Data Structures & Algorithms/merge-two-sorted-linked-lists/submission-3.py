# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        p1 = list1
        p2 = list2
        if p1.val < p2.val:
            head = p1
            l = head
            p1 = p1.next
        else:
            head = p2
            l = head
            p2 = p2.next

        while p1 and p2:
            if p1.val < p2.val:
                l.next = p1
                p1 = p1.next
                l = l.next
            else:
                l.next = p2
                p2 = p2.next
                l = l.next
        if not p1:
            l.next = p2
        else:
            l.next = p1
        return head
            