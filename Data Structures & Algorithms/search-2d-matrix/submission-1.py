class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix) - 1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                row = i-1
                break
        if row < 0:
            return False

        for i in range(len(matrix[row])):
            if matrix[row][i] == target:
                return True
        
        return False
        
