from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result=[]
        if(n%2==0):
            for i in range(1,int(n/2 +1)):
                result.append((i))
                result.append((-i))
        else:
            for j in range(1, int(n / 2 + 1)):
                result.append((j)   )
                result.append((-j))
            result.append(0)
        return result
main =Solution()
print(main.sumZero(3))