class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse() # 1 solution
        left = 0
        right = len(s)- 1

        for i in range(len(s)):
            if left < right:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left +=1
                right -=1
                
        