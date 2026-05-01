class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        left = right = 0
        res  = ""

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                res+=s[left]
                right += 1
            left += 1

        return len(t) - len(res)