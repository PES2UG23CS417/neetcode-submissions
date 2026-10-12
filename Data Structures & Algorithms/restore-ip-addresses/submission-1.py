class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 256 choices for each of the 4 spots 
        # The order of s stays the same
        # we just place the "." in between
        res = []
        if len(s) > 12:
            return res

        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            
            if dots > 4:
                return
            
            # i is where we are at in the string s
            # i is going to tell where we are going to begin and j is going to point to where we are going to end
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, curIP + s[i:j+1] + ".")

        backtrack(0, 0, "")
        return res