class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        n = len(nums)
        MOD = 10**9+7
        cnt = 0

        left = 0
        right = n-1

        while left <= right:
            if nums[left]+nums[right] <= target:
                cnt += pow(2, right - left, MOD)
                left+=1
            else: right-=1
        
        return cnt% MOD

        


        