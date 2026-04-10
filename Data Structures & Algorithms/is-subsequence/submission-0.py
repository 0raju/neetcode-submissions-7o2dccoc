class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        left = fast = 0
        test = ""

        while left < len(s) and fast<len(t):
            if s[left] == t[fast]:
                test+=t[fast]
                left+=1
            fast+=1

        return s==test


        