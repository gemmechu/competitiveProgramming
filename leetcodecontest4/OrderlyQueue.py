class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if(K==1):
            result=[]
            s=S
            for i in range(len(S)):
                s=s[1:]+s[0]
                result.append(s)

            return min(result)
        else:
            s=sorted(S)
            return ''.join(s)

S = ""
K = 2
main=Solution()
print(main.orderlyQueue(S,K))
