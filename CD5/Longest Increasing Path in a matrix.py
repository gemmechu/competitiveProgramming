class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        
        def dfs(i,j):
            nonlocal result,dp
            if dp[i][j] >0:
                return dp[i][j]
            curr_max = 0
            for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0<=x< len(matrix) and 0 <= y< len(matrix[0]):
                    if matrix[i][j] < matrix[x][y]:
                            curr_max = max(curr_max,dfs(x,y))
            dp[i][j] = curr_max + 1
            return dp[i][j]

        result = 0
        for i in range(n):
            for j in range(m):
                result = max(result,dfs(i,j))
                
        # print(dp)
        return result
        
