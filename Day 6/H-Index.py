from typing import List
def hIndex(citations: List[int]) -> int:
    n=len(citations)
    result=0
    citations.sort()
    for j in range(1,n+1):
        count=0
        for i in range(n):
            if citations[i]>=j:
                count+=1
        if count>=j:
            result=max(j,result)
    return result
i = [3,0,6,1,5]
print(hIndex(i))