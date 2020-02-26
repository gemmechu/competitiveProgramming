from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        def checkTurbulance(A, pointer1, pointer2) -> bool:
            # For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
            k = pointer1
            firstPass = True
            for i in range(len(A[pointer1: pointer2+1])-1):
                if(k%2 == 0):
                    if not (A[k] < A[k + 1]):
                        firstPass = False
                        break

                else:
                    if not (A[k] > A[k+1]):
                        firstPass = False
                        break

                k += 1
            # OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd
            if(not firstPass):
                k = pointer1
                for i in range(len(A[pointer1: pointer2 + 1])-1):
                    if (k % 2 == 0):
                        if not (A[k] > A [k + 1]):
                            return False
                    else:
                        if not (A[k] < A[k + 1]):
                            return False

                    k += 1
            return True

        if (len(A) == 1):
            return 1
        pointer1 = 0
        pointer2 = 1

        maxTurbulance = 0
        while pointer2 < len(A):
            ifTurbulance = checkTurbulance(A, pointer1, pointer2)
            if (ifTurbulance):
                temp = pointer2 - pointer1 + 2
                if (maxTurbulance < temp):
                    maxTurbulance = temp
                pointer2 += 1

            else:

                pointer1 = pointer2
                pointer2 += 1

            if (len(A) > 1 and maxTurbulance == 0):
                maxTurbulance = 1


        return maxTurbulance

main = Solution()
a = [4,8,12,16]
print(main.maxTurbulenceSize(a))
