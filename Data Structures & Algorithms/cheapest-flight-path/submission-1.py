from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        

        for i in range(k+1):
            temp = prices.copy()
            for a,b,c in flights:
                if prices[a] == float("inf"):
                    continue
                
                if prices[a]+c<temp[b]:
                    temp[b] = prices[a] + c
                
            prices=temp
        
        if prices[dst] != float("inf"):
            return prices[dst]
        else:
            return -1
                    
                

                






        