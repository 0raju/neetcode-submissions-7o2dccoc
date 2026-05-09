class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # left = 0 # O(n*n)
        # right = 1
        # res = [0]*len(temperatures)
        # while left < len(temperatures):
        #     right = left + 1
        #     while right < len(temperatures):
        #         if temperatures[right] > temperatures[left]:
        #             res[left] = right - left
        #             break
        #         right += 1
        #     left += 1

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev

            stack.append(i)

        return res
