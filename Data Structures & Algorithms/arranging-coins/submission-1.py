class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n < 2:
            return n

        cnt, i = 0, 1
        while i<n:
            new_n = n-i
            if i<n:
                cnt+=1
                i+=1
            n = new_n
        
        return cnt