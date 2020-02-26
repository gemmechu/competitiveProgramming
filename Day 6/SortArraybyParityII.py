from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        result = [0] * len(A)
        oddPointer = 1
        evenPointer = 0
        for i in range(0, len(A)):
                if (A[i] % 2 == 0):
                    result[evenPointer] = A[i]
                    evenPointer += 2
                else:
                    result[oddPointer] = A[i]
                    oddPointer += 2
        return (result)