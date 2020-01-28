class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        if(s ==""):
            return s
        if(len(s)>0):
            stack.append([s[0],1])
        
        for i in range(1,len(s)):
            if(len(stack)==0):
                stack.append([s[i],1])
            else:
                if(s[i]== stack[-1][0]):
                    stack[-1][1] +=1
                    if(stack[-1][1] == k):
                        stack.pop(-1)
                else:
                    stack.append([s[i],1])
        
        return "".join(str(item) for innerlist in stack for item in innerlist[0]*innerlist[1])

                    

a= Solution()
s = "deeedbbcccbdaa" 
k = 3
print(a.removeDuplicates(s,k))