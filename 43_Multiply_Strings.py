class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        product_arr = [0] * (len(num1) + len(num2))
        
        pos = len(product_arr) - 1
        
        for i in reversed(num1):
            temp_pos = pos
            for j in reversed(num2):
                product_arr[temp_pos] += int(i) * int(j)
                product_arr[temp_pos - 1] += product_arr[temp_pos] // 10
                product_arr[temp_pos]  %= 10
                
                temp_pos -= 1
            pos -= 1
        
        pointer = 0
        
        while(pointer < (len(product_arr)- 1) and product_arr[pointer] == 0):
            pointer += 1
        
        return ''.join(map(str, product_arr[pointer:]))
        
        
        