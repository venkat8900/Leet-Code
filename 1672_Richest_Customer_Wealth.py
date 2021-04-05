class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumi = 0
        maxi = 0
        
        for i in range(len(accounts)):
            sumi = sum(accounts[i])
            if sumi > maxi:
                maxi = sumi
            sumi = 0
        
        return maxi
        