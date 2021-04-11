class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        out = []
        count_p = Counter(p)
        count_s = Counter(s[:len(p) - 1])
        
        for i in range(len(p) - 1, len(s)):
            count_s[s[i]] += 1
            
            if count_s == count_p:
                out.append(i - len(p) + 1)
            
            count_s[s[i - len(p) + 1]] -= 1
            if count_s[s[i - len(p) + 1]] == 0:
                del count_s[s[i - len(p) + 1]]
        
        return out
            
        