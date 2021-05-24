class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3 or arr[0]>=arr[1]:
            return False
			
        uphill = True
        
        for i in range(1,len(arr)):
            if uphill:
                if arr[i-1]>=arr[i]:
                    uphill = False
            if not uphill:
                if arr[i-1]<=arr[i]:
                    return False
        return not uphill
        
        