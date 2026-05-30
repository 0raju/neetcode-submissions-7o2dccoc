class Solution:
    def countBits(self, n: int) -> List[int]:

        def hammingWeight(num):
            count = 0
            while num:
                num &= (num - 1)
                count += 1
            return count

        res = []
        for num in range(n+1):
            res.append(hammingWeight(num))

        return res