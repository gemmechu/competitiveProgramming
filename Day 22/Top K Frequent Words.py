from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int)->List[str]:
        dict={}
        result=[]
        if k<1:
            return []
        if len(words)<=1:
            return words
        for i in words:
            if(dict.get(i)==None):
                dict[i]=1 #dict {'the':1,'day':1,'is':1,'sunny':1}
            else:
                dict[i] +=1#dict {'the':3,'day':1,'is':1,'sunny':1}
        
        for i in range(k):
            n=max(dict) #the
            result.append(n) #['the']
            dict.pop(n) #{day':1,'is':1,'sunny':1}
            if(len(dict)==0):
                break
        return result
        
a= Solution()
inputa=[]
k = 1
result=a.topKFrequent(inputa,k)
print(result)

#cont hash input


