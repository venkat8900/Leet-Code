class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        strings = [str(nums) for nums in num]
        str_num = "".join(strings)
        int_str_num = int(str_num)
        
        out_num = int_str_num + k
        
        res = [int(x) for x in str(out_num)]
        
        return res
        