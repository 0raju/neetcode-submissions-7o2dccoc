class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) > 1:
                return n