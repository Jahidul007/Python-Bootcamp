
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def preorder(self, root: 'Node'):

        if not root:
            return []

        result = []
        # approach: use recursion to visit all children
        # if root.children:
        for child in root.children:
            result.extend(self.preorder(child))
        return [root.val] + result