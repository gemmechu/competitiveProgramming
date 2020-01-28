class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if (num<=2):
            return False
        m=int(num/2)
        sum=0
        for i in range(1,m+1):
            if(num%i==0):
                sum+=i
        if(sum == num):
            return True
        else:
            return False
a =Solution()
num=100000000
print(a.checkPerfectNumber(num))
