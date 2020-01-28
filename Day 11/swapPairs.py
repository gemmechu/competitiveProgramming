from typing import List
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if(head ==None or head.next == None):
            return head
        temp=head
        head = head.next
        while temp:
            left=temp
            right=temp.next
            if(right==None):
                break
            a =right.next
            if(a==None):
                left.next=a
            else:
                if(a.next==None):
                    left.next=a
                else:    
                    left.next=a.next
            right.next=left
            if(a != None):
                temp=a
            else:
                break
        return head
main = Solution()
a= ListNode(1)
b= ListNode(3)
c= ListNode(4)
d= ListNode(7)
e= ListNode(9)
f= ListNode(4)
e.next=a
a.next=c
c.next=b
b.next=d

#[9,1,4,3,7,4]

head=main.swapPairs(b)
temp=head
while (temp):
    print(temp.val)
    temp=temp.next
