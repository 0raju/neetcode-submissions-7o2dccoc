class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        neg = []
        pos = []
        result = [0]*len(nums)
        for n in nums:
            if n<0:
                neg.append(n)
            else:
                pos.append(n)
        result[::2], result[1::2] = pos, neg
        return result
        