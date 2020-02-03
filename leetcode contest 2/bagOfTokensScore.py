from typing import List
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        score=0
        maxScore=0
        i=0
        tokens=sorted(tokens)
        while i<len(tokens):
            if(score==0 and P < tokens[i]):
                break
            elif(P>=tokens[i]):
                score+=1
                P-=tokens[i]
                if(maxScore<score):
                    maxScore=score
                i+=1
            elif(score>0):
                score-=1
                P+=tokens[-1]
                tokens.pop(-1)
                
        return maxScore
a=Solution()
tokens =[81,91,31]
p = 73
print(a.bagOfTokensScore(tokens,p))