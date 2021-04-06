class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sumi = 0
        high = int(math.sqrt(num)) + 1
        if num <= 0:
            return False
        
        for i in range(1, high):
            if num%i == 0:
                sumi += i
                if i*i != num:
                    sumi += num/i
        
        return num == (sumi - num)