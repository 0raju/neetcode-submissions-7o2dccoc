class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        left = right = 0
        res  = ""

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                res+=s[left]
                left += 1
            right += 1

        return s == res

        

