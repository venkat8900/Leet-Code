class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        l1 = len(arr)
        arr = sorted(arr)
        l = int(l1 * 0.05)
        return sum(arr[l:l1 - l])/(l1 - 2*l)
        