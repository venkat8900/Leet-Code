class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = {}
        out = []
        for i in nums1:
            counts1[i] = counts1.get(i, 0) + 1
        
        
        for i in nums2:
            if i in counts1 and counts1[i] > 0:
                out.append(i)
                counts1[i] -= 1
        
        return out
            
        
        