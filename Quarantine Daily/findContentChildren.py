class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i,j = 0,0
        cnt = 0
        while True:
            if i >= len(g) or j >= len(s):
                break
            if g[i] <= s[j]:
                cnt += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return cnt
