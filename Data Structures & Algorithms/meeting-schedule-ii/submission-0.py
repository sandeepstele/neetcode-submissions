"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        l=[]

        for i in intervals:
            l.append([i.start,i.end])
        l.sort()

        heap = []

        for start, end in l:
            if heap and heap[0]<=start:
                heapq.heappop(heap)
            heapq.heappush(heap,end)

        
        return len(heap)


    
