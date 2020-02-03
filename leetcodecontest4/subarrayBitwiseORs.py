from functools import reduce
from typing import List


class Solution:
    def subarrayBitwiseORs(self, A: List[int])-> int:
        j=1
        result=set()
        while j<len(A)+1:
            i=0
            while i < len(A):
                if(len(A[i:i+j])==j):
                    value=self.BitwiseORs(A[i:i+j])
                    result.append(value)
                i+=1
            j+=1

        return len(result)

    def BitwiseORs(self, param):
        if(len(param)==1):
            return param[0]
        else:
            res = reduce(lambda x, y: x | y, param)
            return res



a= Solution()
arr1 =[0]
answer=a.subarrayBitwiseORs(arr1)
print(answer)




'''

binaryList=[]
        result=''
        maximum=0
        for i in range(len(A)):
            n=len(bin(A[i])[2:])
            if(maximum<n):
                maximum=n

            binaryList.append(bin(A[i])[2:])
        for k in range(len(binaryList)):
            currentlen=len(binaryList[k])
            if(currentlen<maximum):
                zerotobeadded=maximum-currentlen
                binaryList[k]= (zerotobeadded*'0')+binaryList[k]
        print(binaryList)
        j = 0
        while j<maximum:
            oneFound=False
            for i in range(len(binaryList)):
                mylen=len(binaryList[i])
                if(mylen>j):
                    if(binaryList[i][j]=='1'):
                        result+='1'
                        oneFound=True
                        break
            if(not oneFound):
                result+='0'
            j+=1
        print(result)
        result1=int("110",2)
        return (result1)

'''