from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def isOnBorder(i, j):
            return i==0 or i==len(grid)-1 or j==0 or j == len(grid[0])-1

        def neighbours(i, j):
            for ni, nj in (i+1,j), (i-1,j),(i,j+1),(i,j-1):
                yield ni, nj

        def isInBorder(x, y):
            return (0<=x<len(grid) and 0<=y<len(grid[0]))


        def dfs(i, j):
            grid[i][j] =1
            for x,y in neighbours(i,j):
                if(isInBorder(x,y) and grid[x][y] == 0):
                    dfs(x,y)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0 and isOnBorder(i,j):
                    dfs(i,j)
        closedIslands=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    dfs(i,j)
                    closedIslands+=1
        return (closedIslands)



grid =[[1,0,1]]
a=Solution()
a.closedIsland(grid)