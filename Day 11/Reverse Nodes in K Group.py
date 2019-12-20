class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:     
        now  = head
        prev  = None
        group_count = 0
        prev_tail = dummy = ListNode(-999)
        prev_tail.next = head  # if size of entire list <k , return head 
        
        def reverse(prev,curr, k):
            last_head = curr
            while  k:
                temp = curr.next
                curr.next = prev
                prev = curr 
                curr = temp
                k -=1 
            return last_head, curr,prev
        def get_group_size(curr,n):
            k = 0
            while curr and k < n:curr = curr.next ; k += 1
            return k
        while now and get_group_size(now, k) % k == 0:
            new_tail,now,prev = reverse(None, now, k)
            new_tail.next = now
            prev_tail.next =  prev
            prev_tail = new_tail
            group_count += 1         
        return  dummy.next

