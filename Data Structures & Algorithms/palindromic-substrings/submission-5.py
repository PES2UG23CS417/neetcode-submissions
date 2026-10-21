class Solution:
    def countSubstrings(self, s: str) -> int:
        # optimal
        # res = 0

        # for i in range(len(s)):
        #     # expand and search for odd length palindromes
        #     l = r = i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r += 1

        #     # expand and search for even length palindromes
        #     l = i
        #     r = l + 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         res += 1
        #         l -= 1
        #         r += 1
        
        # return res

        ## same soln as above but since the while loop part is repeated work, we can also condense that work into a function
        res = 0

        for i in range(len(s)):
            res += self.countPal(i, i, s)
            res += self.countPal(i, i+1, s)
        
        return res


    def countPal(self, l, r, s):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        return count
