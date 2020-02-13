from typing import List





class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        result=0
        seen=set()

        def dfs(i):
            for j in range(len(M[i])):
                if M[i][j]==1 and (j not in seen):
                    seen.add(j)
                    dfs(j)

        for i in range(len(M)):
            if i not in seen:
                result+=1
                dfs(i)
        return result

main=Solution()
n=[[1,1,0],
 [1,1,0],
 [0,0,1]]
print(main.findCircleNum(n))