from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        indegree= [0]*(numCourses)
        graph=defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        q=deque()

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        

        taken=[]
        while q:
            course=q.popleft()
            taken.append(course)
            for i in graph[course]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        if len(taken)==numCourses:
            return taken
        else: 
            return []


        




        


        