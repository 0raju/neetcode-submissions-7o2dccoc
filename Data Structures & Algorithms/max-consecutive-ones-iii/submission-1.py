class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # window = [] # option 1 inefficent
        # res = 0

        # for n in range(len(nums)):
        #     window.append(nums[n])
        #     if len(window) - sum(window) <= k:
        #         res = max(res, len(window))
        #     else:
        #         window = window[1:]

        # return res


        left = 0
        res = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros+=1
            if zeros>k:
                if nums[left] == 0:
                    zeros-=1
                left+=1
            res = max(right-left+1, res)
        
        return res


