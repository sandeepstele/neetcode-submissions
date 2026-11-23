class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mp=0

        left,right=0,1

        while right<len(prices):

            cp=prices[right]-prices[left]

            if cp>mp:
                mp=cp
            
            if cp<0:
                left=right
            
            
            right+=1
        return mp
        