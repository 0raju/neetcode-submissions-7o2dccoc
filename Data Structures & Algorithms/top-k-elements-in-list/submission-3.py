class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = []
        i=0
        for i in range(k):
            value = max(set(nums), key=nums.count)
            res.append(value)
            nums = [x for x in nums if x != value]

        return res