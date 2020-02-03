from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0

        newstack = [] 
        for x in pushed: 
            newstack.append(x) 
            while len(newstack)>0 and newstack[-1] == popped[j]: 
                
                newstack.pop() 
                j = j + 1

        return j == len(popped) 


a=Solution()

pushed = [1, 2, 3, 4, 5] 
popped = [4, 5, 3, 2, 1] 
c=a.validateStackSequences(pushed, popped)
print(c)
