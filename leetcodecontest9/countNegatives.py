from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]<0):
                    count += 1
        return count

main=Solution()
grid =[[2],[-1,-3]]
print(main.countNegatives(grid))
