class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # return list(set(nums1).intersection(set(nums2)))

        s = set(nums2)
        res = []

        for n in list(set(nums1)):
            if n in s:
                res.append(n)
        
        return res



        