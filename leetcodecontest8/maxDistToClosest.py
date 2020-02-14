import math
from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
            maxsum=0
            tempsum=0
            index=0
            if(len(seats)==0):
                return 0
            if(seats[0]==0):
                for i in range(len(seats)):
                    if(seats[i]==0):
                        tempsum+=1
                    else:
                        if(tempsum>maxsum):
                            maxsum=tempsum
                            index=i
                            tempsum=0
                            break
            while index<len(seats):
                if (seats[index] == 0):
                    tempsum += 1
                elif(seats[index]==1 and tempsum>0):
                    if(tempsum==1):
                        if(maxsum<tempsum):
                            maxsum=tempsum
                    else:
                        tempsum=math.ceil( tempsum/2)
                        if(maxsum<tempsum):
                            maxsum=tempsum
                    tempsum=0
                index+=1
            if(tempsum>maxsum):
                maxsum=tempsum
            return maxsum
main=Solution()
Input= [0,1,0,1,0]
print(main.maxDistToClosest(Input))

