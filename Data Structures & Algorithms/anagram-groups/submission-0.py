class Solution:
    # def isAnagram(self, s, t, sub_res, flag_set):
    #     s_dict = {}
    #     t_dict = {}
    #     if(len(s) != len(t)):
    #         return sub_res

    #     for i in range(len(s)):
    #         if(s[i] not in s_dict):
    #             s_dict[s[i]] = 1
    #         else:
    #             s_dict[s[i]] += 1
    #         if(t[i] not in t_dict):
    #             t_dict[t[i]] = 1
    #         else:
    #             t_dict[t[i]] += 1
    #     if(s_dict == t_dict):
    #         if(t not in sub_res):
    #             sub_res.append(t)
    #             flag_set[t] = 1

    #     return sub_res

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = []
    #     flag_set = {}
    #     for word in strs:
    #         flag_set[word] = 0
    #     for i in range(len(strs)-1):
    #         sub_res = []
    #         sub_res.append(strs[i])
    #         flag_set[strs[i]] = 1
    #         for j in range(i+1, len(strs)):
    #             if(flag_set[strs[j]] == 0):
    #                 self.isAnagram(strs[i], strs[j], sub_res, flag_set)
    #         res.append(sub_res)

    #     return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            signature = ''.join(sorted(word))
            anagrams[signature].append(word)

        return list(anagrams.values())
