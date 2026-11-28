import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap=[]

        for a,b in points:
            dis=a*a+b*b
            heapq.heappush(heap,(-dis,a,b))

            if k< len(heap):
                heapq.heappop(heap)
        
        return [[a, b] for i, a, b in heap]

        