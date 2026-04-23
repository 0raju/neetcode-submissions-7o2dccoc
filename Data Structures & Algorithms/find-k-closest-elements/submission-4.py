class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # if len(arr) == k: #O(nlogn)
        #     return arr
        
        # res = []
        # diff = []

        # for n in arr:
        #     diff.append(abs(n-x))

        # lowest_indices = sorted(range(len(diff)), key=lambda i: diff[i])[:k]

        # for i in lowest_indices:
        #     res.append(arr[i])

        # return sorted(res)


        left  = 0
        right = len(arr)-1

        while right - left + 1 > k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left+=1
            else:
                right-=1
        
        return arr[left:right+1]



        
        