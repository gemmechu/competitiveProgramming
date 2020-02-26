class Solution:
    def uniquePaths(self,m:int,n:int)->int:
        if(m==0 and n ==0):
            return 0
        if(m==0 or n ==0):
            return 1
        startArr=[1]*m

        tempArr = startArr.copy()
        for i in range(1,n):
            current=0
            for j in range(m):
                tempArr[j]=current+startArr[j]
                current = tempArr[j]
            startArr=tempArr.copy()
        return tempArr[-1]
m=3
n=7

print(Solution().uniquePaths(m,n))