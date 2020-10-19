import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        mydict = {}
        for s in S:
            if mydict.get(s) != None:
                mydict[s] += 1
            else:
                mydict[s] = 1
        heap = [(-value, key) for key,value in mydict.items()]
        heapq.heapify(heap)
        result = []
        while len(heap) > 1:
            curr = heapq.heappop(heap)
            next = heapq.heappop(heap)
            result.append(curr[1])
            result.append(next[1])
            mydict[curr[1]] -= 1
            mydict[next[1]] -= 1
            if (mydict[curr[1]] > 0):
                curr = (curr[0] + 1, curr[1])
                heapq.heappush(heap,curr)
            if (  mydict[next[1]] > 0):
                next = (next[0] + 1, next[1])
                heapq.heappush(heap,next)
        if heap != []:
            last = heapq.heappop(heap)
            if(mydict[last[1]] > 1):
                return ''
            result.append(last[1])
        return ''.join(result)
