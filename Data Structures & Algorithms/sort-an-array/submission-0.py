class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # using merge Sort
        def mergeSort(start, end):
            if start == end:
                return

            mid = (start + end)//2

            mergeSort(start, mid)
            mergeSort(mid+1, end)

            merge(start, mid, end)

        def merge(start, mid, end):
            temp = []
            i = start
            j = mid + 1
            
            while i <= mid and j <= end:
                if nums[i] < nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            
            if i == mid + 1:
                while j <= end:
                    temp.append(nums[j])
                    j += 1
            else:
                while i <= mid:
                    temp.append(nums[i])
                    i += 1
            
            # fixing these positions in nums
            for i in range(len(temp)):
                nums[i + start] = temp[i]
    
        mergeSort(0, len(nums) - 1)
        return nums