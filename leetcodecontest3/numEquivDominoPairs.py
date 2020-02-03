from typing import List
class Solution:
    def checkEquality(self,i:List[int],j:List[int])->bool:
        if(i[0]==j[0] and  i[1] == j[1]):
            return True
        elif(i[0]==j[1] and  i[1] == j[0]):
            return True
        else:
            return False
    
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        equalno=0
        eqaulist=[]
        dominoes=sorted(dominoes)
        for i in range(len(dominoes)):
            point=0
            n=1
            if(dominoes[i]!=[]):
                for j in range(i,len(dominoes)-1):
                    if(dominoes[j+1]!=[]):
                        if(self.checkEquality(dominoes[i],dominoes[j+1])):
                            point+=n
                            n+=1
                            dominoes[j+1]=[]
                
                
                if(point>0):
                
                    equalno+=point
            
        
        return equalno
a=Solution()
dominoes = [[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]
print(a.numEquivDominoPairs(dominoes))
    