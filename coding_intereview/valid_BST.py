# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left:
            max_value = self.find_max(root.left)
            if max_value >= root.val:
                return False
        if root.right:
            min_value = self.find_max(root.right)
            if min_value <= root.val:
                return False
        valid_left = self.isValidBST(root.left)
        valid_right = self.isValidBST(root.right)
        return valid_left and valid_right

    def find_max(self, root):
        max_v = root.val
        if root.left:
            left_max = self.find_max(root.left)
            if left_max > max_v:
                max_v = left_max
        if root.right:
            right_max = self.find_max(root.right)
            if right_max > max_v:
                max_v = right_max
        return max_v

    """
    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        nodes = []
        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
            
        
        inorder(root)
        for i in range(len(nodes)-1):
            if nodes[i]>=nodes[i+1]:
                return False
        return True
    """