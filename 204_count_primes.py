class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2:
            return 0
        
        arr1 = [True] * n
        arr1[0] = arr1[1] = False
        
        
        for i in range(2, int(n**0.5)+1):
            if(arr1[i]):
                for j in range(i*i, n, i):
                    arr1[j] = False
        
        return sum(arr1)
            
            
        