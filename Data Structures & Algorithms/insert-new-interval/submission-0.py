class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left, right =0,len(intervals)-1

        while left<=right:
            mid= (left+right)//2

            if intervals[mid]<=newInterval:
                left=mid+1
            else:
                right= mid-1
        
        intervals.insert(left,newInterval)

        merged=[intervals[0]]

        for start, end in intervals[1:]:
            if start<= merged[-1][1]:
                merged[-1][1]=max(end, merged[-1][1])
            else:
                merged.append([start,end])
        
        return merged



        

        

        
        