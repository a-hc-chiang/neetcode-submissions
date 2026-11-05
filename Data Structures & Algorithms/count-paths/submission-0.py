class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: 
            return 1
        # intializing grid: 

        matrix = [] # m = rows, n = cols 
        for i in range(m):
            to_add = []  
            for j in range(n): 
                to_add.append(0)
            matrix.append(to_add)

        # intializing default values
        for i in range(2, m+1): 
            matrix[m-i][-1] = 1
        for i in range(2, n+1): 
            matrix[-1][n-i] = 1

        # summing result 
        for i in range(1, m): 
            for j in range(1, n): 
                matrix[m-i-1][n-j-1] = matrix[m-i][n-j-1] + matrix[m-i-1][n-j]
        # print(matrix)
        return matrix[0][0]