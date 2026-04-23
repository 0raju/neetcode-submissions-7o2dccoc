class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if len(arr) == k:
            return arr
        
        res = []
        diff = []

        for n in arr:
            diff.append(abs(n-x))

        lowest_indices = sorted(range(len(diff)), key=lambda i: diff[i])[:k]

        for i in lowest_indices:
            res.append(arr[i])

        return sorted(res)

        
        