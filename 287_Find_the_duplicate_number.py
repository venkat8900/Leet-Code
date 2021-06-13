class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [0] * len(nums)
        for i in range(len(nums)):
            if temp[nums[i] - 1] == 0:
                temp[nums[i] - 1] = 1
            else:
                return nums[i]
        