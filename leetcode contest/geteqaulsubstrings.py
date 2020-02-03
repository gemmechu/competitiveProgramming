class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length=min(len(s),len(t))
        lenses=[]
        for j in range(length):
            lenses.append(abs(ord(s[j])-ord(t[j])))
       
        count=0
        curent_count=0
        max_sum=0
        start_index=0
        k=0
        while k < len(lenses) and start_index<len(lenses):
            max_sum+=lenses[k]
            if max_sum<=maxCost:
                curent_count+=1
                k+=1
            else:
                max_sum-=lenses[start_index]
                start_index+=1
                k+=1
                # curent_count-=1
            if count<curent_count:
                count=curent_count
        
        return count
class classname(object):
    pass
s="krpgjbjjznpzdfy"
t="nxargkbydxmsgby"
maxCost =14
print(a.equalSubstring(s,t,maxCost))