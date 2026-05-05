class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            left = nums[i - 1] if i > 0 else float('-inf')
            right = nums[i + 1] if i < len(nums) - 1 else float('-inf')

            if nums[i] > left and nums[i] > right:
                return i
        