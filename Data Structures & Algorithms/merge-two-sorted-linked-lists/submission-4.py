# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
            
        p1, p2 = list1, list2
        if list1.val <= list2.val:
            head = p1
            last = p1
            p1 = p1.next
        else:
            head = p2     
            last = p2
            p2 = p2.next

        while p1 and p2:
            if p1.val > p2.val:
                last.next = p2
                last = last.next
                p2 = p2.next
            else:
                last.next = p1
                last = last.next
                p1 = p1.next
        
        if not p1 and p2:
            last.next = p2
        elif not p2 and p1:
            last.next = p1
        return head