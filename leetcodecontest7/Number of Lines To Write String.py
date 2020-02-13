from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line=0
        lastSum=0
        tempSum=0
        for i in range(len(S)):
            index=ord(S[i])-97
            tempSum+=widths[index]
            lastSum = tempSum
            if(tempSum==100):
                tempSum=0
                line+=1
            elif(tempSum>100):
                tempSum=widths[index]
                line+=1
            if(i == len(S)-1):
                if(tempSum>0):
                    line+=1
                    lastSum=tempSum




        result=[line,lastSum]
        return result
main=Solution()
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S =  "abcdefghijklmnopqrstuvwxyz"
print(main.numberOfLines(widths,S))



