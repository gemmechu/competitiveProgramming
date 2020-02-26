def anagram1(s1:str, s2:str)->bool:
    #O(nlogn)
    s1 = s1.replace(' ','')
    s2 = s2.replace(' ', '')
    if (len(s1) != len(s2)):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    return s1 == s2

def anagram2(s1:str, s2:str)->bool:
    #O(n)
    s1 = s1.replace(' ','')
    s2 = s2.replace(' ', '')
    if(len(s1)!=len(s2)):
        return False
    mydict={}
    for i in range(len(s1)):
        if(s1[i] in mydict):
            mydict[s1[i]] += 1
        else:
            mydict[s1[i]] = 1
    for j in range(len(s2)):
        if (s2[j] in mydict):
            mydict[s2[j]] -= 1
        else:
            return False
    for k in mydict:
        if(mydict[k]!=0):
            return False
    return True

s1="govd"
s2="dodg"
print(anagram2(s1, s2))
