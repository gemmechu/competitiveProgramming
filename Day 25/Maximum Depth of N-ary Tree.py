# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    max_depth = 0
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
           return 0
        def getMaxDepth(node, depth):
            if root:
                self.max_depth = max(depth, self.max_depth)
                for i in root.children:
                    getMaxDepth(i, self.depth+1)
            else:
                return
        getMaxDepth(root)
        return self.max_depth






'''

'''
