from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        mydict={}
        for i in range(len(richer)):
            if(mydict.get(richer[i][1])!=None):
                mydict[i] = mydict[i].append(richer[i][0])
            else:
                mydict[i]=[richer[i][0]]
        print(mydict)

        return None
main=Solution()
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
main.loudAndRich(richer,quiet)