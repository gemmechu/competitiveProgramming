from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        top=[]
        left=[]
        result=0
        for i in range(len(grid)):
            left.append(max(grid[i]))
            for j in range(len(grid[i])):
                if(i==0):
                    top.append(grid[i][j])
                else:
                    top[j]=max(top[j],grid[i][j])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                bothside=min(top[j],left[i])
                result+=bothside-grid[i][j]


        return result
main=Solution()
grid = [[1,2,3]]
print(main.maxIncreaseKeepingSkyline(grid))