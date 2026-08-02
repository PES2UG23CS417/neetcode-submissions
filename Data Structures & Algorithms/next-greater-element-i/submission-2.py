class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = [-1]*len(nums1)

        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):

        #         if nums1[i] == nums2[j]:
        #             k = j + 1
        #             while k < len(nums2):
        #                 if nums2[k] > nums2[j]:
        #                     res[i] = nums2[k]
        #                     break
        #                 k += 1
                        
        #             break
        # return res

        # Sol 2: More optimal
        stk = []
        nextGreater = {}

        for n in nums2:
            while stk and n > stk[-1]:
                nextGreater[stk.pop()] = n
            stk.append(n)
        
        while stk:
            nextGreater[stk.pop()] = -1
        
        return list(nextGreater[n] for n in nums1)