from typing import List
from operator import add
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        monoIncreasing=True
        monoDecreasing = True
        if(len(A)==0):
            return False
        for i in range(len(A)-1):
            if(A[i]>A[i+1]):
                monoIncreasing=False

        if(monoIncreasing==False):
            for j in range(len(A)-1):
                if (A[j] < A[j + 1]):
                    monoDecreasing=False
        if(monoDecreasing or monoIncreasing == True):
            return True
        else:
            return False

a= Solution()
arr1 =[1,3,2]
#[2,2,2,1,4,5]

print(a.isMonotonic(arr1))