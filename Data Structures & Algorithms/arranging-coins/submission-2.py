class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # if n < 2:
        #     return n

        # cnt, i = 0, 1
        # while i<n:
        #     new_n = n-i
        #     if i<n:
        #         cnt+=1
        #         i+=1
        #     n = new_n
        
        # return cnt

        left, right = 1, n
        res = 0

        while left <= right:
            mid = left + (right - left) // 2
            coins_needed = mid * (mid + 1) // 2
            if coins_needed <= n:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res        


