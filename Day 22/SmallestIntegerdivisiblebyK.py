class Solution:
    def gcd(self,x,y):
        while(y):
            x,y=y, x%y
        return x

    def smallestKint(self,n):
        result=1
        for i in range(1,n+1):
            result = (result * i)/self.gcd(i,result)
        print(int(result))
a= Solution()
a.smallestKint(10)