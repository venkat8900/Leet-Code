class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        out = []
        dict_p = {}
        dict_s = {}
        for p1 in p:
            dict_p[p1] = dict_p.get(p1, 0) + 1
        
        for s1 in s[:len(p)-1]:
            dict_s[s1] = dict_s.get(s1, 0) + 1
            
        for i in range(len(p) - 1, len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            
            if dict_s == dict_p:
                out.append(i - len(p) + 1)
            
            dict_s[s[i-len(p)+1]] -= 1
            
            if dict_s[s[i-len(p)+1]] == 0:
                del dict_s[s[i-len(p)+1]]
        return out
            
        