class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
def printLevel(root: Node, result, level: int):
    if root:
        if len(result) < level+1:
            result.append([])

        printLevel(root.left, result, level+1)
        result[level].append(root.val)
        printLevel(root.right, result, level + 1)
    return result
def levelOrderPrint(root: Node):
    if not root:
        return
    currentCount = 1
    childrenCount =0
    deque = [root]
    while len(deque) > 0:
        root = deque.pop()
        print(root.val,)
        currentCount -= 1
        if root.left:
            deque.insert(0,root.left)
            childrenCount += 1
        if root.right:
            deque.insert(0, root.right)
            childrenCount += 1
        if currentCount == 0:
            currentCount, childrenCount = childrenCount, 0
            print("\n")
root= Node(4)
a= Node(7)
b= Node(3)
c= Node(5)
d= Node(2)
e = Node(8)
root.left = b
root.right = a
a.left = c
b.left = d
b.right =e
levelOrderPrint(root)
#print(result)