from typing import List


class Solution:
    def findLongestChain(self,pairs: List[List[int]]):
        result=0

        for i in range(len(pairs)):
            tempArray = [pairs[i][1]]
            for j in range(i+1,len(pairs)):
                if(pairs[j][0] not in tempArray):
                    tempArray.append(pairs[j][0])
            if(len(tempArray)>result):
                result=len(tempArray)


        return result
main=Solution()
a=[[1,1,1],[1,1,1]]
print(main.findLongestChain(a))
