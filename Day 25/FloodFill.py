from typing import List




class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        value = image[sr][sc]
        def neighbours(i, j):
            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                yield ni, nj

        def inbound(x, y):
            result= (0<=x<len(image) and 0<=y<len(image[0]))

            return result

        def dfs(i, j):
            image[i][j]=newColor
            for x,y in neighbours(i,j):
                if(inbound(x,y)==True):
                    if(image[x][y]==value):
                        dfs(x,y)

        if(len(image)==0):
            return image
        if(newColor==image[sr][sc]):
            return image

        dfs(sr,sc)
        return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
main=Solution()
print(main.floodFill(image,sr,sc,newColor))