class Solution:
    def power(self,x,y):
        if(y==0):
            print(1)
            return
        if(x==0):
            print(0)
            return
        result=1
        flag=False
        if(y<0):
            y*=-1
            flag=True
        for i in range(y):
            result*=x
        if(flag):
            print(1/result)
        else:
            print(result)
a= Solution()
x=2
y=2
a.power(x,y)