class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res=[1]*len(nums)
        n,pre,suf=len(nums),1,1

        for i in range(n):
            res[i]=pre
            pre=pre*nums[i]
        
        for j in range(n-1,-1,-1):
            res[j]*=suf
            suf=suf*nums[j]
        return res

