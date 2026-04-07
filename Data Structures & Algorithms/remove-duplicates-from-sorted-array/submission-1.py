class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = slow + 1
        while fast <len(nums):
            if (nums[slow] == nums[fast]):
                nums.remove(nums[fast])
            else:
                slow +=1
            fast = slow + 1
        return len(nums)
            



        