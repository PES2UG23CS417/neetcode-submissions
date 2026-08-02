class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x,y,z = m-1,m+n-1,n-1

        while x>= 0 and z >= 0:
            if nums2[z] > nums1[x]:
                nums1[y] = nums2[z]
                z -= 1
            else:
                nums1[y] = nums1[x]
                x -= 1
            y -= 1
        
        if x < 0:
            while z >= 0:
                nums1[y] = nums2[z]
                z -= 1
                y -= 1
        else:
            while x >= 0:
                nums1[y] = nums1[x]
                y -= 1
                x -= 1
        