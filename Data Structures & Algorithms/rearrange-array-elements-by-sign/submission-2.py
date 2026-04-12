class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        neg = []
        pos = []
        for n in nums:
            if n<0:
                neg.append(n)
            else:
                pos.append(n)
                
        nums[::2], nums[1::2] = pos, neg
        return nums
        