class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        # window = arr[:k]

        # if sum(window)/len(window)>threshold :
        #     res = 1
        # else: 
        #     res = 0

        # for i in range(k, len(arr)):
        #     if arr[i] > arr[i-k]:
        #         window = arr[i-k+1:i+1]
        #         if sum(window)/len(window)>threshold:
        #             res+=1
        res = 0

        for i in range(len(arr)-k+1):
            window = arr[i:i+k]
            if sum(window)/len(window)>=threshold:
                res+=1
        return res


        