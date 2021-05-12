class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(digits) for digits in digits]
        a_string = "".join(strings)
        an_integer = int(a_string)
        
        out_integer = an_integer + 1
        res = [int(x) for x in str(out_integer)]
        
        return res
            
        