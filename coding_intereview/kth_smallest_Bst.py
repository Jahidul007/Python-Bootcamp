# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nodes = []
        self.inorder(root)
        return nodes[k - 1]

        # use this method without memory consideration
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            nodes.append(root.val)
            inorder(root.right)
            print(nodes)





        # use this for O(K) memory
        def inorder1(root):
            nonlocal k
            if root is None:
                return
            val = inorder1(root.left)
            if val:
                return val
            if k == 1:
                return root.val
            k -= 1
            return inorder1(root.right)

        return inorder1(root)
