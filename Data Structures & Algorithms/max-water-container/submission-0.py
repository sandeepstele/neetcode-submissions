class Solution:
    def maxArea(self, heights: List[int]) -> int:

        mw,left,right=0,0,len(heights)-1

        while left<right:

            mw=max(mw,min(heights[left],heights[right])* (right-left))

            if heights[right]>heights[left]:
                left+=1
            
            else:
                right-=1
        return mw

        