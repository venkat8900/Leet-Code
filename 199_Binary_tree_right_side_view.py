# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        q = [root]
        out = []
        
        while q:
            n = len(q)
            
            for i in range(1, n+1):
                temp = q[0]
                q.pop(0)
                
                if (i == n):
                    out.append(temp.val)
                
                if temp.left:
                    q.append(temp.left)
                
                if temp.right:
                    q.append(temp.right)
        
        return out
                    
        