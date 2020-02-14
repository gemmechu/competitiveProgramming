from typing import List


class Solution:
    def shiftingLetters(self, S, shifts):
        aa = ord('a')
        ll = len(shifts)
        ss = list(S)[:ll]

        for i in range(1, len(shifts), 1):
            shifts[ll - 1 - i] += shifts[ll - i]
        # print(shifts)
        for i in range(len(shifts)):
            ss[i] = chr((ord(ss[i]) - aa + shifts[i]) % 26 + aa)
        return ''.join(ss)
    '''
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
        return result'''
main=Solution()
S = "ruu"
shifts = [26,9,17]

print(main.shiftingLetters(S,shifts))