#!/bin/python3

import os
import sys
import heapq
#
# Complete the cookies function below.
#
def cookies(k, A):
    heapq.heapify(A)
    try:
        cnt = 0
        while A[0] < k:
            cnt += 1
            c1,c2 = heapq.heappop(A),heapq.heappop(A)
            new = c1 + (2*c2)
            heapq.heappush(A, new)
        return cnt
    except:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
