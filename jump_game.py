class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_jump = 0
        n = len(nums) - 1
        i = 0
        
        while(i <= max_jump and i < n):
            if max_jump >= n:
                break
            
            max_jump = max(max_jump, i + nums[i])
            i += 1
        return max_jump >= n
        
        