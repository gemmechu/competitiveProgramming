
from typing import List
class CustomFunction:
    
    def f(self,x,y):
        return x+y
class Solution:
    def findSolution(self,customfunction:CustomFunction,z:int):
        result=[]
        x=1
        while x<=z:
            
            lower=1
            upper=z
            while lower<=upper:
                mid=int((lower+upper)/2)
                f=customfunction.f(x,mid)
                if(f==z):
                    a=[x,mid]
                    
                    result.append(a)
                    break
                elif f<z:
                    lower=mid+1
                else:
                    upper=mid-1
            x+=1
        return result
a=Solution()
c=CustomFunction()
print(a.findSolution(c,5))