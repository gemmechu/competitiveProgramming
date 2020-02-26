from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if (len(events) < 1):
            return 0
        if (len(events) == 1):
            return 1
        maxEvent = events[0][0]
        orgcount = 0
        for i in range(len(events)):
            if events[i][0] <= maxEvent and maxEvent <= events[i][1]:
                maxEvent += 1
                orgcount += 1
        events = sorted(events)
        maxEventS = events[0][0]
        countS = 0
        for j in range(len(events)):
            if events[j][0] <= maxEventS and maxEventS <= events[j][1]:
                maxEventS += 1
                countS += 1
        print(countS)
        print(orgcount)
        return max(countS, orgcount)

events = [[1,5],[1,5],[1,5],[2,3],[2,3]]
main= Solution()
print(main.maxEvents(events))