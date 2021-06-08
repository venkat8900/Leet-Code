# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        self.helper(root, out)
        return out
    
    def helper(self, root, out):
        if root:
            out.append(root.val)
            self.helper(root.left, out)
            self.helper(root.right, out)
        