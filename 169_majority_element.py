class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        count = 1
        temp = nums[0]
        for num in nums[1:]:
            if num == temp:
                count += 1
            elif count == 0:
                temp = num
                count = 1
            else:
                count -= 1
        
        return temp
        