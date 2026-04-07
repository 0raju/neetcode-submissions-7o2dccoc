class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sorted_num = sorted(set(nums))
        longest = 1
        all_time = 1

        for i in range(1, len(sorted_num)):
            if sorted_num[i] - sorted_num[i-1] == 1:
                longest +=1
                if longest> all_time:
                    all_time = longest
            else: 
                longest=1
        return all_time
 


        