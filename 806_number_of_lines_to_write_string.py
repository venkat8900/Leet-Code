class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        pixels = 0
        lines = 1
        
        for i in s:
            w = widths[ord(i) - ord('a')]
            
                
            if (pixels + w) > 100:
                pixels =  w
                lines += 1
            else:
                pixels = pixels + w
        
        return [lines, pixels]
            
            
            
        