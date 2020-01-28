from typing import List
import math
class Solution:
    def countPrimes(self,n:int)->int:
        if (n<=2):
            return 0
        primes=[True for i in range(n)]
   

        for i in range(2,int(math.sqrt(n-1)+1)):
            if(primes[i]):
                j=i+i
                while j<n:
                    primes[j]=False
                    j+=i
        count=0
        for i in range(2,n):
            if(primes[i]):
                count+=1
        return count
main=Solution()
print(main.countPrimes(20))

                
