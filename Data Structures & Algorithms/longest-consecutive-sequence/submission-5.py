class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()
        res = 1
        cnt = 1

        for left in range(1, len(nums)):
            if nums[left] == nums[left-1]+1:
                cnt +=1
                res = max(res, cnt)
            else:
                cnt=1
        
        return res



        