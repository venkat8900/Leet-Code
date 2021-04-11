
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        tree= [root]
        depth = 0
        while tree:
            depth += 1
            for i in range(len(tree)):
                temp = tree.pop(0)
                if temp.left:
                    tree.append(temp.left)
                if temp.right:
                    tree.append(temp.right)
        return depth
        
        
        