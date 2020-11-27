class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def getCount(num):
            nonlocal add
            if num <= 0:
                return 0
            
            if num % 2 != 0:
                add += 1
                num -= 1
                
            return 1 + getCount(num/2)
        
        
        add = 0
        mult = 0
        for i in nums:
            mult = max(mult,getCount(i) -1)
            
        return mult + add 
            
