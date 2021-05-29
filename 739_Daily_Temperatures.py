class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures) -1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            
            if stack and temperatures[i] < stack[-1][0]:
                res[i] = stack[-1][1] - i
            
            stack.append([temperatures[i], i])
                                                                                                        
        
        
        return res
        