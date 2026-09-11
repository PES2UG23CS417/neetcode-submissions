class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}
        # seen = set()
        res = []

        for i in range(len(s)):
            last_seen[s[i]] = i

        l, r = 0, 0
        while r < len(s):
            # seen.add(s[r])
            if last_seen[s[r]] > r:
                idx = last_seen[s[r]]
                r += 1
                while r < idx:
                    # seen.add(s[r])       
                    if last_seen[s[r]] > idx:
                        idx = last_seen[s[r]]
                    r += 1
            res.append(r-l+1)
            l = r + 1
            r += 1
        
        return res