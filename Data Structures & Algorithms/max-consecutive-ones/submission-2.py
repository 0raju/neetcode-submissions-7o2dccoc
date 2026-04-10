class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        global_max = 0
        current = 0
        for left in range(len(nums)):
            if nums[left] == 1:
                current +=1
                global_max = max(global_max, current)
            else:
                current=0
            left +=1
    
        return global_max
            
                
        