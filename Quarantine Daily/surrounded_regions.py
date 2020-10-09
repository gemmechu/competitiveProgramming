class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def inbound(i,j):
            if (0<=i<len(board) and 0<=j< len(board[0])):
                return True
            return False
        
        def neighbours(i,j):
            for ni, nj in (i-1,j), (i+1,j),(i,j+1),(i,j-1):
                if (inbound(ni,nj)):
                    if (board[ni][nj] == 'O'):
                        yield ni,nj
                    
        def dfs(i,j):
            board[i][j] = '1'
            n = neighbours(i,j)
           
            for neighbour in n :
                
                x,y = neighbour
                dfs(x,y)
        def isBoarder(i,j):
            if(i == 0 or i == len(board)-1):
                return True
            elif(j == 0 or j == len(board[0]) -1):
                return True
            return False
        zeros = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == 'O' and isBoarder(i,j)):
                    dfs(i,j)
                        
                        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == 'O'):
                    board[i][j] = 'X'
                
                elif(board[i][j] == '1'):
                    board[i][j] = 'O'
                        
        return board
                        
                    
