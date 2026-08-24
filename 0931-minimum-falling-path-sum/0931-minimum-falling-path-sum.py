class Solution(object):  
  
    def minFallingPathSum(self, matrix):  
  
        """  
        :type matrix: List[List[int]]  
        :rtype: int  
        """  
  
        n = len(matrix)  
        memo = [[None] * n for _ in range(n)] 
 
        def s(i, j):  
            if j < 0 or j >= n:  
                return float('inf') 
 
            if memo[i][j] is not None: 
                return memo[i][j] 
  
            if i == n - 1:  
                return matrix[i][j]  
  
            LD = matrix[i][j] + s(i + 1, j - 1)  
            D = matrix[i][j] + s(i + 1, j)  
            RD = matrix[i][j] + s(i + 1, j + 1) 
 
            memo[i][j] = min(LD, D, RD)  
            return memo[i][j] 
 
        return min(s(0, j) for j in range(n))