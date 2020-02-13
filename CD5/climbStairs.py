
class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        beforeprev=1
        for i in range(2, n):
            beforeprev = prev
            prev += beforeprev

        return prev + beforeprev




a=[1,2,1,4]
print(min(a))