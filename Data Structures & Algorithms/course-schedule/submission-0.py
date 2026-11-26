from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree= [0]*(numCourses)
        graph=defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        q=deque()

        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        

        taken=0
        while q:
            course=q.popleft()
            taken+=1
            for i in graph[course]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return taken==numCourses

        




        