"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        out = []
        if root == None:
            return out
        self.helper(root, out)
        return out
    
    def helper(self, root, out):
        for child in root.children:
            self.helper(child, out)
        out.append(root.val)
        