class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort()
        n=len(nums)
        

        res=[]


        for i in range(n-2):
            left,right=i+1,n-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue


            while left<right:
                
                total =nums[left]+nums[right]+nums[i]


                if total>0:
                    right-=1
                
                elif total<0:
                    left+=1

                else:

                    res.append([nums[left],nums[i],nums[right]])

                    right-=1
                    left+=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res

                