class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        best_sum = nums[0]

        for n in nums:
            if curr_sum <0:
                curr_sum = 0
            curr_sum+=n

            best_sum = max(best_sum, curr_sum)

        return best_sum



        