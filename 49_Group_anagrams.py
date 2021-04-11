class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        y = {}
        
        for s in strs:
            key = tuple(sorted(s))
            y[key] = y.get(key, []) + [s]
        
        return y.values()
                
            
                
                
            
            
            
        
        
        