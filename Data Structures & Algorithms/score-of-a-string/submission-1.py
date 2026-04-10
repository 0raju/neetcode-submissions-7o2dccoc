class Solution:
    def scoreOfString(self, s: str) -> int:

        score = 0
        n = len(s)

        for left in range(n-1):
            score+= abs(ord(s[left]) - ord(s[left+1]))
            left+=1
        
        return score
        