'''
[-1,3,2,0,4,6]
a = [-1,-1,-1,-1,-1]
c = [-1,3,3,3,4,6]
b = [-1,0,0,0,4,6]

[-1,3,2,0]
a = [-1,-1,-1,-1]
c = [-1,3,3,3]
b = [-1,0,0,0]

[1,2,3,4]
[1,1,1,1]
[1,2,3,4]
[1,2,3,4]

[3,1,4,2]
[3,1,1,1]
[3,3,4,4]
[1,1,2,2]
     
'''


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return False
        a,b,c= [None]*n,[None]*n,[None]*n
        n -= 1
        for i,num in enumerate(nums):
            if i ==0:
                a[i] = num
                b[n] = nums[n]
                c[i] = num
            else:
                a[i] = min(a[i-1],num)
               
                c[i] = max(num,c[i-1])
                num = nums[n-i]
                b[n-i] = min(b[n-i+1],num)
        stack = []
        for i in range(n,-1,-1):
            if( nums[i] > a[i] ): 
                while( stack and stack[-1] <= a[i] ):
                    stack.pop()
                if(stack and a[i] < stack[-1] < nums[i] ):
                    return True
                    
                stack.append(nums[i])
        return False
            
