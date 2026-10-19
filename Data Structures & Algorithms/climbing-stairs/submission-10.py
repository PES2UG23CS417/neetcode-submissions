class Solution:
    def climbStairs(self, n: int) -> int:
        # # Bottom up solution
        # prev2, prev1 = 1, 1

        # for step in range(n-2, -1, -1):
        #     current = prev1 + prev2
        #     prev2 = prev1
        #     prev1 = current
        
        # return prev1

        ## repeat
        step1, step2 = 1, 1

        for i in range(n-2, -1, -1):
            current = step1 + step2
            step2 = step1
            step1 = current
        
        return step1