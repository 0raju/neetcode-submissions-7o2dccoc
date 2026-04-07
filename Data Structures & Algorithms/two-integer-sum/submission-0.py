class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valid = {}

        for idx,value in enumerate(nums):
            if target-value in valid:
                return [valid[target-value], idx]
            else:
                valid[value] = idx
            
        