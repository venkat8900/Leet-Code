"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue = [root]
        res = collections.deque()
        
        if root is None:
            return []
        
        
        
        while(queue):
            next_level = []
            res.append([])
            for node in queue:
                res[-1].append(node.val)
                for child in node.children:
                    next_level.append(child)
            queue = next_level
        
        return list(res)
            
        