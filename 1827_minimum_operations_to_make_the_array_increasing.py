class Solution:
    def minOperations(self, nums: List[int]) -> int:
        temp = nums[0]
        count = 0
        
        
        for i in range(1, len(nums)):
            if nums[i] < temp:
                diff = temp - nums[i] + 1
                nums[i] += diff
                count += diff
                temp = nums[i]
            
            elif nums[i] == temp:
                nums[i] += 1
                temp = nums[i]
                count += 1
            
            else:
                temp = nums[i]
        
        return count
    
    
    