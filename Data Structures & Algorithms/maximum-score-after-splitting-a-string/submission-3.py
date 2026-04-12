class Solution:
    def maxScore(self, s: str) -> int:

        left_zeros = s[:1].count('0') # option 1
        right_ones = s[1:].count('1')
        max_score = left_zeros + right_ones
        for i in range(1, len(s)-1):
            if s[i] =='0':
                left_zeros +=1
            else:
                right_ones -=1
            max_score = max(max_score, left_zeros + right_ones)

        return max_score

        