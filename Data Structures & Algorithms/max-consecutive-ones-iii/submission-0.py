class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        window = []
        res = 0

        for n in range(len(nums)):
            window.append(nums[n])
            if len(window) - sum(window) <= k:
                res = max(res, len(window))
            else:
                window = window[1:]

        return res
