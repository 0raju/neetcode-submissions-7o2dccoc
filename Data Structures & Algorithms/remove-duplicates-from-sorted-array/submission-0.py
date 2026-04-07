class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = slow + 1
        while fast <len(nums):
            if (nums[slow] == nums[fast]):
                nums.remove(nums[fast])
                fast = slow +1
            else:
                slow +=1
                fast = slow +1
        return len(nums)
            



        