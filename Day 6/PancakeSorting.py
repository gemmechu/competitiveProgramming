from typing import List


class Solution:
    def pancakeSort(self,A:List[int])-> List[int]:

        def iterater(A, end , B):

            mi = A.index(len(A[:end]))
            reversed(A[0:end])
            B.append(len(A[:end]))
            return mi
        end= len(A)
        B= []
        while end:
            iterater(A,end, B)
            end-=1
        return B