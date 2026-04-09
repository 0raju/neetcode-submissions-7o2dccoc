class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)
        # slow = 0

        for slow in range(len(nums)):
            fast = 0
            while fast < len(nums):
                if slow != fast:
                    result[slow] = result[slow] * nums[fast]
                fast+=1
        return result

        