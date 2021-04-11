class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                temp = stones[-1] - stones[-2]
                stones.pop()
                stones.pop()
                stones.append(temp)
        
        if len(stones) != 0:
            return stones[0]
        else:
            return 0
        