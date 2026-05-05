class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)      
        res = right

        while left <= right:
            k = left + (right-left)//2
            hour = 0
            for p in piles:
                hour += math.ceil(p/k)
            if hour <=h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res

