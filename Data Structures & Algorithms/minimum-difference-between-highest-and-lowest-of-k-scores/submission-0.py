class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()

        res = []

        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]) - min(nums[i:i+k]))

        return min(res)
        