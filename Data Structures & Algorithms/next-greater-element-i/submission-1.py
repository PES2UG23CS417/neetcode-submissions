class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)

        for i in range(len(nums1)):
            for j in range(len(nums2)):

                if nums1[i] == nums2[j]:
                    k = j + 1
                    while k < len(nums2):
                        if nums2[k] > nums2[j]:
                            res[i] = nums2[k]
                            break
                        k += 1
                        
                    break
        return res