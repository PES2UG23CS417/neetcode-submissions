class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()

        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

        for i in range(k, len(nums)):
            res.append(nums[q[0]])
            while q and q[0] <= i - k:
                q.popleft()
            
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        
        res.append(nums[q[0]])
        return res