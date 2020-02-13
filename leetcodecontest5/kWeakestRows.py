from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier=[]
        result=[]
        for i in range(len(mat)):
            soldier.append(mat[i].count(1))
        maxsold=max(soldier)+1
        for j in range(k):
            value= min(soldier)

            index=soldier.index(value)
            result.append(index)
            soldier[index]=maxsold
        return result
main= Solution()
a=[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
print(main.kWeakestRows(a,3))
