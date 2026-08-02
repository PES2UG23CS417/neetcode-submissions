class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l, r = 0, 0
        window = 0
        res = 0
        while r < len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = 1
            else:
                hashmap[s[r]] += 1
            window += 1
            if (window - max(hashmap.values()) <= k):
                res = max(window, res)
            else:
                hashmap[s[l]] -= 1
                l += 1
                window -= 1
            r += 1
        return res