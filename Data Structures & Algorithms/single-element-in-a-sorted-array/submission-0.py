class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xorr = 0
        for n in nums:
            xorr ^= n
        return xorr


        