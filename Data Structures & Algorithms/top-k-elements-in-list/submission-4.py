from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter= Counter(nums)

        bucket=[[] for _ in range(len(nums)+1)]

        for num,freq  in counter.items():

            bucket[freq].append(num)
        
        results=[]

        for freq in range(len(nums),0,-1):
            for nums in bucket[freq]:
                results.append(nums)
                if len(results)==k:
                    return results

      
        