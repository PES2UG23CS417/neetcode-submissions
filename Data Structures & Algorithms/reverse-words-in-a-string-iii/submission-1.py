class Solution:
    def reverseWords(self, s: str) -> str:
        # li = s.split()

        # for i in range(len(li)):
        #     li[i] = li[i][::-1]
        
        # return " ".join(li)

        # even more efficient
        return " ".join(word[::-1] for word in s.split())