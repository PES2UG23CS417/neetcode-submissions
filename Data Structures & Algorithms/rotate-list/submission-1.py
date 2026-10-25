# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # # 3 pointers - prev, h2, tail
        # if not head or not head.next or k == 0:
        #     return head

        # tail = head
        # count = 1
        # while tail.next:
        #     count += 1
        #     tail = tail.next
        
        # k = k % count
        # if k == 0:
        #     return head

        # i = 0
        # h2 = head
        # print(count)
        
        
        # while i < (count - k):
        #     prev = h2
        #     h2 = h2.next
        #     i += 1
        # print(head.val, prev.val, h2.val, tail.val)
        
        # tail.next = head
        # prev.next = None

        # return h2

        ### most efficient
        if head == None or head.next == None or k == 0:
            return head
        
        tail = head
        count = 0
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