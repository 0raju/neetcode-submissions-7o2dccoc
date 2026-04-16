class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # res = 0 # option-1

        # for i in range(len(arr)-k+1):
        #     window = arr[i:i+k]
        #     if sum(window)/len(window)>=threshold:
        #         res+=1

        target = threshold * k
        window = sum(arr[:k])
        res = 1 if window>=target else 0

        for i in range(k, len(arr)):
            window += arr[i] - arr[i-k]
            if window>=target:
                    res+=1
        return res


        