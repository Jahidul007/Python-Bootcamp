# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: 
            return 0
        sum = 0
        if L <= root.val <= R: 
            sum += root.val
        if L < root.val: 
            sum += self.rangeSumBST(root.left, L, R)
        if R > root.val: 
            sum += self.rangeSumBST(root.right, L, R)
        return sum 
