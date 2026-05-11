class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row = len(matrix) - 1
        # for i in range(len(matrix)):
        #     if matrix[i][0] > target:
        #         row = i-1
        #         break
        # if row < 0:
        #     return False

        # for i in range(len(matrix[row])):
        #     if matrix[row][i] == target:
        #         return True
        
        # return False
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows*cols -1

        while left<=right:
            mid = left + (right-left)//2
            r = mid // cols
            c = mid % cols
            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False