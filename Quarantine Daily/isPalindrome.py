# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        values = []
        while head != None:
            values.append(head.val)
            head = head.next
        
        reverse =list( reversed(values))
        
        if(values == reverse):
            return True
        return False
