from typing import List


class Solution:
    def allCellsDiOrder(self, R : int, C : int, r0: int, c0 : int)-> List[List[int]]:
        result=[]
        for i in range(R):
            for j in range(C):
                result.append([abs(r0-i), abs(c0-j)])
        return result
main= Solution()
R=2
C=2
r0=0
c0=1
print(main.allCellsDiOrder(R,C,r0,c0))