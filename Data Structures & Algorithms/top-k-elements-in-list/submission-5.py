from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counter =Counter(nums)

        bucket=[[] for _ in range(len(nums)+1)]

        for a,b in counter.items():
            bucket[b].append(a)
        
        result=[]

        for i in range(len(nums),0,-1):
            for j in bucket[i]:
                result.append(j)

                if len(result)==k:
                    return result