from collections import deque


"""5 solutions in python(From Easy to Hard)"""
"""https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/266632/5-solutions-in-python(From-Easy-to-Hard)"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """recursively"""
        if not root:
            return []

        res = []
        self.recurse(root, 0, res)
        return res

    def recurse(self, root, level, res):
        if not root:
            return

        if len(res) < level + 1:
            res.append([])

        res[level].append(root.val)
        self.recurse(root.left, level + 1, res)
        self.recurse(root.right, level + 1, res)


class Solution3:
    def levelOrder(self, root: TreeNode):
        """bfs + queue"""
        if root is None:
            return []

        res = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if len(res) < level + 1:
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return res
