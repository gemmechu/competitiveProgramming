class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if(len(row)>0):
                if(row[0]<= target <= row[-1]):
                    if(target in row):
                        return True
        return False
