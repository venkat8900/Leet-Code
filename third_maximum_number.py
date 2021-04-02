class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        max1 = max2 = max3 = -float(inf)
        
        for i in nums:
            if i in (max1, max2, max3):
                continue
            if i > max1:
                i, max1 = max1, i
            
            if i > max2:
                i, max2 = max2, i
            
            if i > max3:
                i, max3 = max3, i
            
        return max1 if max3 == -float(inf) else max3
        
        
        
        