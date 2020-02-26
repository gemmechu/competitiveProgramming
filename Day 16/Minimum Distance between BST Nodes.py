from typing import List

from leetcodecontest4.IncreasingBST import TreeNode


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def helper(root: TreeNode, result: List[int]):
            if root:
                helper(root.left, result)
                result.append(root.val)
                helper(root.right, result)
            return result
        result = helper(root,[])

        if(len(result)>1):
            minimum = abs(result[1] - result[0])
            for i in range(len(result)):
                for j in range(len(result)):
                    if(i == j):
                        continue
                    else:
                        temp_diffrence = abs(result[i] - result[j])
                        if(temp_diffrence < minimum):
                            minimum = temp_diffrence
            return minimum
        else:
            return 0
