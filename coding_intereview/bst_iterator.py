# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    stk = []

    def __init__(self, root: TreeNode):
        node = root
        while node:
            self.stk.append(node)
            node = node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        next_val = self.stk[-1].val
        node = self.stk.pop()
        if node.right:
            node = node.right
            while node:
                self.stk.append(node)
                node = node.left
        return next_val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stk != []

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()