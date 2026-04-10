class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        left = 0
        while left < (len(arr)-1):
            arr[left] = max(arr[left+1:])
            left+=1
        
        arr[len(arr)-1] = -1

        return arr

            




