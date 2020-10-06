# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        
        length = 0
        curr = head
        while curr != None:
            curr = curr.next
            length  += 1
        
       
        if(n == length):
            return head.next
        
        curr = head
        for i in range(length-n):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        return head 
