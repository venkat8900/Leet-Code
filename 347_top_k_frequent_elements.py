from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using bucket sort
        bucket = [[] for i in range(len(nums) + 1)] # creates an empty list with frequencies tilllen(nums)
        
        # create a counter to get frequencies of numbers
        count = Counter(nums)
        
        for num, freq in count.items():
            bucket[freq].append(num)
        
        out = list(chain(*bucket))
        
        return out[::-1][:k]
        
        
        
        
                
            
        
        
        
        
        
        