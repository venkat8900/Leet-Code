class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        out = []
        
        
        left = [0] * len(boxes)
        
        count = int(boxes[0])
        for i in range(1, len(boxes)):
            left[i] = left[i -1] + count
            count += int(boxes[i])
            
        right = [0] * len(boxes)
        count = int(boxes[-1])
        
        for i in range(len(boxes) - 2, -1, -1):
            right[i] = right[i + 1] + count
            count += int(boxes[i])
        
        for i in range(len(boxes)):
            out.append(left[i] + right[i])
        
        return out
        
            
            
        
                
            
        