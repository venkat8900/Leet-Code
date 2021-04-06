from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = Counter(nums)
        for k,i in a.items():
            if i < 2:
                return k