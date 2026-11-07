class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)

        res = 0

        for n in nums:
            if n-1 not in s:
                cnt = 1
                while n+cnt in s:
                    cnt+=1
                res = max(res, cnt)
        return res

        