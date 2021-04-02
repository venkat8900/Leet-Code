class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        
        if len(a) != len(b) or set(a) != set(b):
            return False
        
        if a == b:
            return len(a) - len(set(a)) >= 1
        
        l1 = []
        count = 0
        
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
                l1.append(i)
            
            if count > 2:
                return False
        return a[l1[0]] == b[l1[1]] and a[l1[1]] == b[l1[0]]
            
            
        