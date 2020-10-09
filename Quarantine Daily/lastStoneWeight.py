import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def smash_stone(stones):
            if len(stones) < 2:
                return stones
            y,x = -(heapq.heappop(stones)),-(heapq.heappop(stones))
            if(y>x):
                new =-(y-x)
                heapq.heappush(stones,new)
            return smash_stone(stones)
        stones = [ -x for x in stones]
        heapq.heapify(stones)
        result = smash_stone(stones)
        if (len(result) == 0):
            return 0
        return -(result[0])
    
