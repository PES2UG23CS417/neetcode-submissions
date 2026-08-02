class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Bruteforce
        # res = []
        # window = []

        # for r in range(len(nums)):
        #     window.append(nums[r])
        #     if len(window) == k:
        #         res.append(max(window))
        #         window.pop(0)
        # return res

        # Single Pass Neetcode solution
        # output = []
        # q = collections.deque() # index
        # l = r = 0
        # while r < len(nums):
        #     # pop smaller values from q
        #     while q and nums[q[-1]] < nums[r]:
        #         q.pop()
        #     q.append(r)

        #     # remove left val from window 
        #     if l > q[0]:
        #         q.popleft()
        #     if (r + 1) >= k:
        #         output.append(nums[q[0]])
        #         l += 1
        #     r += 1
        # return 
        
        ##
        # nums = [1,2,1,0,4,2,6]
        
        ## Solution 3 (not single pass but equally optimal)
        res = []
        q = collections.deque()

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        
        for j in range(k, len(nums)):
            res.append(nums[q[0]])

            while q and q[0] <= j - k:
                q.popleft()
            
            while q and nums[q[-1]] <= nums[j]:
                q.pop()
            q.append(j)
        
        res.append(nums[q[0]])
        return res