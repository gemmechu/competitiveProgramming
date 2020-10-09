class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [ [0 for i in range(len(colSum))] for j in range(len(rowSum))]        
       
        i,j = 0,0
        while True:
            if(i >= len(rowSum) or j>=len(colSum)):
                break
                
            curr = min(rowSum[i], colSum[j])
            matrix[i][j] = curr
            
            
            rowSum[i] -= curr
            colSum[j] -= curr
            if(rowSum[i] == 0):
                i += 1
            if(colSum[j] == 0):
                j += 1
        return matrix
