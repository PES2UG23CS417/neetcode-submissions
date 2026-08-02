class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        nextGreater = {}
        res = []
        for n in nums2:
            while stk and n > stk[-1]:
                nextGreater[stk.pop()] = n
            stk.append(n)
        
        while stk:
            nextGreater[stk.pop()] = -1
        
        return list(nextGreater[n] for n in nums1)

        stk = []
        nextGreater = {}

        for n in nums2:
            while stk and n > stk[-1]:
                nextGreater[stk.pop()] = n
            stk.append(n)
        
        while stk:
            nextGreater[stk.pop()] = -1
        
        for n in nums1:
            res.append(nextGreater[n])
        
        return res