# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # O(n) time and space complexity solution
        # l = head
        # res = []
        # while l is not None:
        #     res.append(l.val)
        #     l = l.next
        # l, r = 0, len(res) - 1
        # while (l < r):
        #     if res[l] != res[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        ##
        # O(n) time and O(1) space complexity solution
        fast = head
        slow = head
        # to find middle = slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        