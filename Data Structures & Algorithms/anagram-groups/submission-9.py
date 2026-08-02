class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            rec = [0]*26
            for c in s:
                rec[ord(c) - ord('a')] += 1
            res[tuple(rec)].append(s)
        
        return list(res.values())
