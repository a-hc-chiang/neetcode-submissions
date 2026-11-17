class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix) # rows 
        n = len(matrix[0]) # cols
        left, right = 0, m*n  - 1 # ending "index"

        while left <= right: 
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target: 
                return True
            elif matrix[row][col] > target: # we're too big
                right = mid - 1 
            else: # we're too small 
                left = mid + 1 
        return False