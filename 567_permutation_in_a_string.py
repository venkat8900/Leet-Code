class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = {}
        dict_s2 = {}
        
        for i in s1:
            dict_s1[i] = dict_s1.get(i, 0) + 1
        
        for j in s2[:len(s1) - 1]:
            dict_s2[j] = dict_s2.get(j, 0) + 1
        
        for i in range(len(s1) - 1, len(s2)):
            dict_s2[s2[i]] = dict_s2.get(s2[i], 0) + 1
            if dict_s2 == dict_s1:
                break
            
            dict_s2[s2[i - len(s1) + 1]] = dict_s2.get(s2[i - len(s1) + 1], 0) - 1
            
            if(dict_s2[s2[i - len(s1) + 1]] == 0):
                del dict_s2[s2[i - len(s1) + 1]]
        return dict_s2 == dict_s1
            
            
        