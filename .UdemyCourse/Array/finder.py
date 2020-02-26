import collections


def finder1(arr1, arr2) -> int:
    #O(n)
    mydict = {}
    for i in range(len(arr1)):
        if (arr1[i] in mydict):
            mydict[arr1[i]] += 1
        else:
            mydict[arr1[i]] = 1
    for j in range(len(arr2)):
        mydict[arr2[j]] -= 1

    for k in mydict:
        if (mydict[k] != 0):

            return k
    return None
def finder2(arr1, arr2) -> int:
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    for num1,num2 in zip(arr1,arr2):
        if (num1 != num2):
            return num1
def finder3(arr1, arr2) -> int:
    d = collections.defaultdict(int)
    for num in arr2:
        d[num] += 1

    for num in arr1:
        if(d[num]) == 0:
            return num
        else:
            d[num] -= 1
a=[3,1,4,6,2,1]
b=[6,1,3,1,4]
print(finder2(a,b))