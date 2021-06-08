# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        
        q = [root]
        
        while q:
            temp = q[0]
            q.pop(0)
            
            if temp:
                temp.left, temp.right = temp.right, temp.left
                q.append(temp.left)
                q.append(temp.right)
            
            
                
        
        return root
    
    
    
    
   
        
        
        