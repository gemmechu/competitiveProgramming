class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        def get_circle(start, end,cnt):
            m = []
            if(start<end):
                m = [x for x in range(start, end)] 
            else:
                m = [x for x in range(start, cnt+1)]
                for x in range(1,end): m.append(x)
            return m
        result = {}
        for i in range(1,n+1):
            result[i] = 0
       
        x = 0
        y = 1
        cnt = n
        max = 0
        for j in range(len(rounds)):
            start = rounds[x]
            if(len(rounds) == j+1):
                result[start] = result[start] + 1
                if(max< result[start]):
                    max = result[start]
                continue
            end = rounds[y]
            m = get_circle(start, end, cnt)
            
            for k in m:
                result[k] = result[k] + 1
                if(max< result[k]):
                    max = result[k]
            final = []
            
            x += 1
            y += 1
        for item in result:
                if(result[item] == max):
                    final.append(item)
       
        return final
solution = Solution()
solution.mostVisited(2,[2,1,2,1,2,1,2,1,2])
