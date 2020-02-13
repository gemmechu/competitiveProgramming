from typing import List




class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def neighbours(i, j):
            for ni, nj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),(i-1, j - 1),(i+1, j + 1),(i+1, j - 1),(i-1, j + 1):
                yield ni, nj

        def isInBorder(x, y):
            return (0 <= x < len(board) and 0 <= y < len(board[0]))

        def dfs(i,j):
            if(board[i][j]=='M'):
                board[i][j] ='X'
                return board

            for x,y in neighbours(i,j):

                if(isInBorder(x,y) and board[x][y] == 'E'):
                    if(board[x][y]=='M'):
                        if (board[i][j] == 'E'):
                            board[i][j] = '1'
                        elif (board[i][j] != 'M' and board[i][j] != 'B'):
                            board[i][j] = str(int(board[i][j]) + 1)
                    else:
                        if (board[i][j] == 'E'):
                            board[i][j] = 'B'
                    dfs(x,y)
            return board
        return dfs(click[0],click[1])
main=Solution()
board=[['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'M', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E'],
        ['E', 'E', 'E', 'E', 'E']]
click=[0,2]
print(main.updateBoard(board,click))

