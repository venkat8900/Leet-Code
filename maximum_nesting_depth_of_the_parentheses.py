class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        count = 0
        l1 = []
        
        for i in s:
            if i == "(":
                l1.append("(")
                count += 1
                maxi = max(count, maxi)
            
            if i == ")":
                l1.pop()
                count -= 1
            
        return maxi