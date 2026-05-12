class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d = {}
        stack = []

        for num in nums2:
            while stack and num> stack[-1]:
                d[stack.pop()] = num
            stack.append(num)

        res = []
        for n in nums1:
            res.append(d.get(n, -1))
        
        return res

        
        # d = dict()
        # res = []
        # d[nums2[-1]] = - 1

        # for i in range(len(nums2)-2, -1, -1):
        #     j = i+1
        #     while j<len(nums2):
        #         if nums2[i] < nums2[j]:
        #             d[nums2[i]] = nums2[j]
        #             break
        #         j+=1
        
        # for n in nums1:
        #     res.append(d.get(n, -1))
        
        # return res