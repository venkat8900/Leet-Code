class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s1 = []
        s2 = []
        
        s1.append(edges[0][0])
        s1.append(edges[0][1])
        s2.append(edges[1][0])
        s2.append(edges[1][1])
        
        if s1[0] in s2:
            return s1[0]
        else: 
            return s1[1]
        
        
        
            
        