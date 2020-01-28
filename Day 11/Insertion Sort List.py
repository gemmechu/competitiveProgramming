# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        boundary=head
        check=head.next
        while check:
            if check.val>=boundary.val:
                boundary=boundary.next
                check=check.next
            elif head.val<=check.val and check.val<=boundary.val:
                temp=head
                while not (temp.val<=check.val and check.val<=temp.next.val):
                    temp=temp.next
                #swap
                newChk=check.next
                check.next=temp.next
                temp.next=check
                boundary.next=newChk
                check=newChk
            else:
                newChk=check.next
                check.next=head
                head=check
                boundary.next=newChk
                check=newChk
        return head
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

head=main.insertionSortList(e)
temp=head
while (temp):
    print(temp.val)
    temp=temp.next


