from typing import List


class Solution:
    def longestPalindrome(self,s:str)->str:
        grid= [[0 for i in range(len(s))] for j in range(len(s))]
        maxlen = 0
        result = []
        if(len(s)==0):
            return ""
        for i in range(len(s)):
            grid[i][i]=1
            maxlen=1
            result=[0,0]
        for j in range(len(s)-1):
            if(s[j]==s[j+1]):
                maxlen=2
                grid[j][j+1]=1
                result=[j,j+1]

        for j in range(2,len(s)):
            for i in range(len(s)-j):
                if(s[i]==s[i+j] and grid[i+1][i+j-1]==1):
                    grid[i][i+j]=1
                    if(maxlen<j):
                        maxlen=j
                        result=[i,i+j]


        return s[result[0]:result[1]+1]
main=Solution()
print(main.longestPalindrome("aab"))