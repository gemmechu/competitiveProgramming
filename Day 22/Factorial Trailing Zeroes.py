class Solution:
    def trailingZeroes(self, n: int) -> int:
        if(n<0):
            return -1
        c=0
        i=5
        while n/i>=1:
            c+= n/i
            i*=5
        return c
a =Solution()
num=14
print(int(a.trailingZeroes(num)))
     
