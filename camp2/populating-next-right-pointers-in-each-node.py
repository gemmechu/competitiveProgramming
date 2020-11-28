"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or root.left == None:
            return root
        q = []
        q.append(root.left)
        q.append(root.right)
        while q:
            new = []
            while q:
                curr = q.pop(0)
                if curr.left != None:
                    new.append(curr.left)
                    new.append(curr.right)
                if q:
                    curr.next = q[0]
                else:
                    curr.next = None
            
            q = new
        return root
                
                
                
        
