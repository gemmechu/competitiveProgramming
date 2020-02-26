from typing import List


class Solution:
    def minPathSum(self,grid: List[List[int]])->int:
        if(not len(grid)>0):
            return 0
        #summing the 1st row
        if(not len(grid[0])>0):
            return 0
        for i in range(1,len(grid[0])):
            grid[0][i]+=grid[0][i-1]
        # summing the 1st column
        for j in range(1, len(grid)):
            grid[j][0] += grid[j-1][0]

        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])

        return grid[-1][-1]
main=Solution()
grid=[[1,2],[3,4],[1,4]]
print(main.minPathSum(grid))