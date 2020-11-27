class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n//10 == 0:
            return str(n)
        result = ''
        cnt = 0
        while n>0:
            l = str(n%10)
            if cnt != 0  and cnt%3 == 0:
                result = '.' + result
            result = l + result
            cnt += 1
            n //= 10
        return result
            
        
