class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # if target > sum(nums):
        #     return 0

        # window_sum = 0
        # res = float('inf')

        # left = 0
        # right = 0

        # while right <(len(nums)):
        #     if window_sum < target:
        #         window_sum +=nums[right]
        #     if window_sum >= target:
        #         res = min(res, right-left+1)
        #         window_sum = window_sum - nums[left]
        #         if window_sum < target:
        #             right+=1
        #         left+=1
        #     else:
        #         right+=1

        # return res

        left =0
        window_sum = 0
        res = float('inf')

        for right in range(len(nums)):
            window_sum +=nums[right]

            while window_sum >=target:
                res = min(res, right - left + 1)
                window_sum -= nums[left]
                left+=1
        
        return res if res != float('inf') else 0









        