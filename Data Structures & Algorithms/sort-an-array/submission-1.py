class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums) - 1

        def mergeSort(start, end):
            # divide
            if start >= end:
                return
            
            if start < end:
                mid = (start + end)//2
                mergeSort(start, mid)
                mergeSort(mid+1, end)
                merge(start, mid, end)

        def merge(start, mid, end):
            # conquer
            temp = []
            i, j = start, mid + 1

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
            
            #find the correct position of the respective elements in the actual array
            for i in range(len(temp)):
                nums[i + start] = temp[i]

        mergeSort(start, end)

        return nums            