
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def postorder(self, root: 'Node'):

        if not root:
            return []

        result = []
        # approach: use recursion to visit all children
        for child in root.children:
            result.extend(self.postorder(child))
        return result + [root.val]