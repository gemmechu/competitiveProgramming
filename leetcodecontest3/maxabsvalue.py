from typing import List
from operator import add
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        a = list( map(add, arr1, arr2) )
        arr2=[x * -1 for x in arr2]
        print(arr2)
        maxpoint= 1
        return maxpoint
a= Solution()
arr1 = [1,-2,-5,0,10]
arr2 = [0,-2,-1,-7,-4]
print(a.maxAbsValExpr(arr1,arr2))