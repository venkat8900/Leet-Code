class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        out = []
        for i in range (1,target[-1] + 1):
            out.append("Push")
            if i not in target:
                out.append("Pop")
        return out
            
 
            
        