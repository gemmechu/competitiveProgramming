class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)-1
        for i in range(n+1):
            if(s[i]==s[n-i]):
                continue
            else:
                return -1
                break
        return 1
    def checkPalindrom(self, s)
a= Solution()
s='abba'
result=a.countSubstrings(s)
print(result)