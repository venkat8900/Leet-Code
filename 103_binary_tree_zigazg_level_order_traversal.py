# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        cur_level = [root]
        out = []
        
        direction = 1
        
        while cur_level:
            level = []
            
            for i in range(len(cur_level)):
                temp = cur_level.pop(0)
                level.append(temp.val)
                
                if temp.left:
                    cur_level.append(temp.left)
                if temp.right:
                    cur_level.append(temp.right)
            
            out.append(level[::direction])
            direction *= -1
            
                
        return out
            
        