class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        leftsum = 0

        for idx in range(len(nums)):
            rightsum = total - nums[idx] - leftsum

            if leftsum == rightsum:
                return idx
            
            leftsum += nums[idx]
        
        return -1

