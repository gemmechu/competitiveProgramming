class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        mydict = {}
        for i in range(len(groupSizes)):
            key = groupSizes[i]
            if(mydict.get(key) !=None):
                mydict[key].append(i)
            else:
                mydict[key] = [i]
        
        result = []
        for key in mydict:
            if key == len(mydict[key]):
                result.append(mydict[key])
            else:
                curr = mydict[key]
                i = 0
                while i < len(curr):
                    result.append(curr[i:i+key])
                    i += key
        return result
                    
            
