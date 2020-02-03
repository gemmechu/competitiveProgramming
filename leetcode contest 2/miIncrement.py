from typing import List
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A=sorted(A)
        count=0
        for i in range(1,len(A)):
            if(A[i]<=A[i-1]):
                count+=A[i-1]-A[i]+1
                A[i]=A[i-1]+1
        return count
            
                    
a=Solution()
aa=[3,2,1,2,1,7]
print(a.minIncrementForUnique(aa))

'''
        Arr=[]
        count=0
        if(len(A)==0):
            return 0
        for i in range(len(A)):
            if(A[i] not in Arr):
                Arr.append(A[i])
                Arr=sorted(Arr)
            else:
                while True:
                    A[i]+=1
                    count+=1
                    if(A[i] not in Arr):
                        Arr.append(A[i])
                        Arr=sorted(Arr)
                        break
        return count
'''