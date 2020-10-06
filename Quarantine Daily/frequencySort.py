class Solution:
    def frequencySort(self, s: str) -> str:
        def maxheap(result, i,N,mydict):
            l = i*2
            r = i*2 +1
            if(l <= N and mydict[result[l]] > mydict[result[i]]):
                largest = l
            else:
                largest = i
            if (r <= N and mydict[result[r]] > mydict[result[largest]]):
                largest = r
            if(largest != i):
                result[i], result[largest] = result[largest],  result[i]
                ma
                xheap(result, largest,N,mydict)
            return result
        if len(s) < 2:
            return s
        
        mydict  = {}
        for c in s:
            if mydict.get(c) != None:
                mydict[c] += 1
            else:
                mydict[c] = 1
        
        result = list(mydict.keys())
        
        result.insert(0,'')
        print(mydict)
        N = len(mydict) 
        print('first',result)
        for i in range(N//2, 0, -1):
            result =  maxheap(result, i,N,mydict)
            print(result)
        
           
        return ''.join([key * mydict[key] for key in result[1:]])
