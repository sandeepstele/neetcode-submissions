
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}
        result=[]
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        

        bucket= [[] for i in range(len(nums)+1)]

        for num,freq in count.items():
            bucket[freq].append(num)


        for freq in range(len(nums),0,-1):
            for num in bucket[freq]:
                result.append(num)
            
                if len(result)==k:
                    return result




        

        