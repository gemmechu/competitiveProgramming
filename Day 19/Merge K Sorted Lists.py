from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    result=ListNode(None)
    def sortedMerge(self,a,b):
        
        if(a== None):
            return b
        if(b== None):
            return a
        if(a.val <= b.val):
            result =a
            result.next= self.sortedMerge(a.next,b)
        else:
            result =b
            result.next= self.sortedMerge(a,b.next)
        return result

    def mergeKLists(self,lists: List[ListNode])-> ListNode:
        last=len(lists)-1
        while last !=0:

            i=0
            j=last
            while (i<j):
                lists[i]=self.sortedMerge(lists[i],lists[j])
            
                i+=1
                j-=1
                if(i>=j):
                    last=j
        return lists[0]
    

main = Solution()
a= ListNode(1)
b= ListNode(4)
c= ListNode(30)

d= ListNode(1)
e= ListNode(9)
f= ListNode(17)

g= ListNode(6)
h= ListNode(9)
i= ListNode(23)
j= ListNode(27)

a.next=b
b.next=c

d.next=e
e.next=f

g.next=h
h.next=i
i.next=j

lists=[a,d,g]


result= main.mergeKLists(lists)

while result !=None:
    print(result.val)
    result=result.next

