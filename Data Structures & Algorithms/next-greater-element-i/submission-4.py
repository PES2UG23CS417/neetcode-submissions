class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nextG = {}
        stk = []
        for n in nums2:
            while stk and stk[-1] < n:
                nextG[stk.pop()] = n
            stk.append(n)
        
        while stk:
            nextG[stk.pop()] = -1
        
        for n in nums1:
            res.append(nextG[n])
        
        return res