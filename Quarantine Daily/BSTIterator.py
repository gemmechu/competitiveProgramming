# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
       
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def dfs(root, result):
            if root:
                
                dfs(root.left, result)
                result.append(root.val)
                dfs(root.right, result)
            return result
        self.root = root
        self.in_order_traversal = dfs(self.root, [])
        self.i = 0
    
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.hasNext():
            result = self.in_order_traversal[self.i]
            self.i += 1
            return result
            
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.i < len(self.in_order_traversal):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
