from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result=[]
        st=[]
        if(len(arr)<=1):
            return True
        for i in range(len(arr)):
            if(arr[i] not in  st):
                count = arr.count(arr[i])
                result.append(count)
                st.append(arr[i])
          
        result.sort()
        for i in range (len(result)):
            if (i<len(result)-1):
                if(result[i]==result[i+1]):
                    return False
                    break
        return True
            
a= Solution()
b= []
c= a.uniqueOccurrences(b)
print(c)
