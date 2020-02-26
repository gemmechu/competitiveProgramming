from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range (len(A)):
            A[i] = A[i] * A[i]
        return  sorted(A)
a = Solution()
print(a.sortedSquares([-7,-3,2,3,11]))
