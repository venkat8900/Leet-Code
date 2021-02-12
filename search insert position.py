class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target == 0:
            return 0
        
        elif target > nums[len(nums) - 1]:
            return len(nums)
        
        count = 0
        for i in range (len(nums)):
            if target > nums[i]:
                count += 1
            else:
                return count
        