class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        sumi = 0
        for i in nums:
            sumi += i
            out.append(sumi)
            
        return out