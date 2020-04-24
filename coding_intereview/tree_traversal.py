# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):
        res = []
        if not root:
            return res
        # Pre order tree traverse
        # res.append(root.val)
        if root.left:
            res.extend(self.postorderTraversal(root.left))
        # IN order tree traverse
        # res.append(root.val)
        if root.right:
            res.extend(self.postorderTraversal(root.right))
        # post order tree traverse
        res.append(root.val)

        return res