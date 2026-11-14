class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)

        stack=[]
        i=0

        while i < len(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev=stack.pop()
                result[prev]=i-prev
            stack.append(i)
            i+=1
        return result