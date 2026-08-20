class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # word_dict = set(wordDict)
        # l, r = 0, 0
        # found = []
        # while r < len(s):
        #     if s[l:r+1] in wordDict:
        #         found.append(s[l:r+1])
        #         l = r+1
        #     r += 1

        # print(wordDict)
        # print(found)
        # text = ""
        # print(set(found) <= set(wordDict))
        # if set(found) <= set(wordDict):
        #     for words in found:
        #         text += words
        #     if text == s:
        #         return True
        # return False

        # Actual Sol: Dynamic Programming
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]