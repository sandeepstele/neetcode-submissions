class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        a=set()
        l=0

        for i in nums:
            a.add(i)

        for num in a:
            if num-1 not in a:
                c=1
                while num+c in a:
                    c+=1
                l=max(l,c)
        return l

                
