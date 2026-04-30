class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for n in nums: # O(n*n)
        #     if nums.count(n) > 1:
        #         return n
        # nums.sort() # O(nlogn)
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]
        # return -1

        seen = set()

        for n in nums:
            if n in seen:
                return n
            seen.add(n)