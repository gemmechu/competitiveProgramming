from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree=[0]*numCourses
        for i in range(len(prerequisites)):
            inDegree[prerequisites[i][0]]+=1
        stack=[]
        for i in range(len(inDegree)):
            if(inDegree[i]==0):
                stack.append(i)
        count=0
        while(len(stack)!=0):
            curr=stack.pop()
            count+=1
            for i in range(len(prerequisites)):
                if(prerequisites[i][1]==curr):
                    inDegree[prerequisites[i][0]]-=1
                    if(inDegree[prerequisites[i][0]]==0):
                        stack.append(prerequisites[i][0])
        return count==numCourses
main=Solution()
n=3
preq=[[1,0],[0,1]]
print(main.canFinish(n,preq))