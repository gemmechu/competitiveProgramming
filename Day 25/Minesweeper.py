from typing import List




class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def neighbours(i, j):
            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),(i-1, j - 1),(i+1, j + 1),(i+1, j - 1),(i-1, j + 1):
                yield ni, nj

        def isInBorder(x, y):
            return (0 <= x < len(board) and 0 <= y < len(board[0]))
        def dfs(board: List[List[str]], click: List[int]) -> List[List[str]]:
            i,j=click[0], click[1]
            if(board[i][j]=='M' and isInBorder(i,j)):
                board[i][j]='X'
                return board
            #check how many M are there

            count = 0
            for x,y in neighbours(i,j):
                if(isInBorder(x,y) and board[x][y]=='M'):
                    count+=1
            if(count>0):
                board[i][j]=str(count)
                return board
            board[i][j]='B'
            #continue DFS
            for x,y in neighbours(i,j):
                if(isInBorder(x,y) and board[x][y] !='B'):
                    dfs(board,[x,y])
            return board
        return dfs(board,click)

main=Solution()
board=[['E', 'E', 'E', 'E', 'E'],
       ['E', 'E', 'M', 'E', 'E'],
       ['E', 'E', 'E', 'E', 'E'],
       ['E', 'E', 'E', 'E', 'E']]
click=[1,2]
print(main.updateBoard(board,click))

