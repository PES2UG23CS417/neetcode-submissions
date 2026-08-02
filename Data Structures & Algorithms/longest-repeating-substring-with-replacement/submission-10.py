class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        res = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            length = r - l + 1
            max_freq = max(freq.values())
            if length - max_freq <= k:
                res = max(res, r-l+1)
            else:
                freq[s[l]] -= 1
                l += 1
        return res