import numpy as np
class Solution:
    def smallestDivisor(self,nums,treshold)->int:
        res= 1
        while True:
            sum=0
            for i in nums:
                sum += np.ceil(i/res)
            if sum<= treshold:
                break  
            res+=1
        return res  
a= Solution()
num=[19]
print(a.smallestDivisor(num,6)) 