# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode, val=0) -> int:
        if not root: return 0
        # sum of binary number
        val = val * 2 + root.val
        """
        sum of decimal number
        val = val * 10 + root.val
        """
        if root.left == root.right:
            return val  # exit
        return self.sumRootToLeaf(root.left, val) + \
               self.sumRootToLeaf(root.right, val)
