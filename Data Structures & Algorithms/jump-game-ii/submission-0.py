class Solution:
    def jump(self, nums: List[int]) -> int:

        left,right,c=0,0,0

   

        while right<len(nums)-1:

            mj=0

            for i in range(left,right+1):
                mj= max(mj,i+nums[i])


            
            left,right=right+1,mj
            c+=1
        return c



            


        