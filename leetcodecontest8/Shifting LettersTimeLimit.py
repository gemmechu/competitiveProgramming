from typing import List


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        if(not(len(S) == len(shifts))):
            return ""
        result=''
        for i in range(len(S)):
            temp=sum(shifts[i:len(S)])

            if(temp>25):
                temp%=26

            shifter = ord(S[i]) + temp
            if(shifter>ord('z')):
                shifter-=ord('z')+1
                shifter+=ord('a')
            result+=chr(shifter)
        return result
main=Solution()
S = "ruu"
shifts = [26,9,17]

print(main.shiftingLetters(S,shifts))