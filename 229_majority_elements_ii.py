class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        m = {}
        out = []
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
                    
            else:
                m[nums[i]] = 1
            
            
        for key, value in m.items():
            if value > (len(nums)/3):
                out.append(key)
        
        return out
                
        