from typing import List


class Solution:
    def minimum(self,triangle:List[List[int]])->int:
        if(len(triangle)==0):
            return 0
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])

        return triangle[0][0]
main=Solution()
triangle=[[1],[2,3,1]]
print(main.minimum(triangle))