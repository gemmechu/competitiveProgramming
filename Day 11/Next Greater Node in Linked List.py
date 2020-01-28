from typing import List
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result=[]
        current=head
        while current:
            temp= current
            while temp:
                if(current.val < temp.val):
                    result.append(temp.val)
                    break
                elif(temp.next == None):
                    result.append(0)
                    break
                temp=temp.next
            current=current.next
                
        return result
main = Solution()
a= ListNode(1)
b= ListNode(3)
c= ListNode(4)
d= ListNode(7)
e= ListNode(9)
e.next=a
a.next=c
c.next=b
b.next=d
#[9,1,4,3,7]

print(main.nextLargerNodes(b))