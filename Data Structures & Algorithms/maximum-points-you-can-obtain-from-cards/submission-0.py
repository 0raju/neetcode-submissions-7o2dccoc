class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) # O(n)
        window = n-k
        curr = sum(cardPoints[:window])

        left_out = curr

        for i in range(window, n):
            curr += cardPoints[i] - cardPoints[i - window]
            left_out = min(left_out, curr)
        
        return sum(cardPoints) - left_out