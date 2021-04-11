class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        k = 5
        
        while k<=n:
            count += n//k
            k = k * 5
        return count
            
        