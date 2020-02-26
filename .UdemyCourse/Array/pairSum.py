from typing import List


def pairSum(mylist:List[int], summation:int)-> int :
    output = set()
    if(len(mylist)<2):
        return output
    seen = set()
    for i in range(len(mylist)):
        current=mylist[i]
        target=summation-current
        if target not in seen:
            seen.add(current)
        else:
            output.add((min(target, current),max(target, current)))
    print(output)
    return len(output)
mylist=[1,3,2,2]
print(pairSum(mylist,4))