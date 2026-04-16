class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums_unique = list(set(nums))

        for n in nums_unique:
            if nums.count(n) > len(nums)//2:
                return n
        