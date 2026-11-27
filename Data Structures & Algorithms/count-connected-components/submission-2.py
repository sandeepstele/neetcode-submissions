
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        parent=list(range(n))
        

        def find(x):

            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            
            return x
        

        def union(a,b):
            ra,rb = find(a), find(b)

            if ra==rb:
                return False
            
            parent[ra]=rb
            return True
        
        comp=n

        for a,b in edges:
            if union(a,b):
                comp-=1
        
        return comp
