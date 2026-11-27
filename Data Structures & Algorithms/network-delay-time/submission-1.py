import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for a,b,c in times:
            graph[a].append((b,c))

        
        heap = [(0, k)]
        dist={}


        while heap:
            time,node =heapq.heappop(heap)

            if node in dist:
                continue
            dist[node] = time           


            for nei,t in graph[node]:
                if  nei not in dist:
                    heapq.heappush(heap, (time + t, nei))
            

        return max(dist.values()) if len(dist) == n else -1
        