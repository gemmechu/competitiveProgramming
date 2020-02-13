from typing import List



class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def neighbours(i):
            for ni in (i + arr[i]), (i - arr[i]):
                    yield ni


        def inbound(x)->bool:
            return  (0 <= x < len(arr))
        def dfs(i,tracker):
            tracker.append(i)
            for x in neighbours(i):
                if (inbound(x) == True):
                    if (x not in tracker):
                        dfs(x,tracker)



        dfs(start,[])

main=Solution()
a=[4,2,3,0,3,1,2]
start = 5
main.canReach(a,start)
