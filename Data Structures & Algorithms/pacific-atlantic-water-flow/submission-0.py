class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


        rows,columns=len(heights),len(heights[0])
        
        pac,atl=set(),set()


        def dfs(r,c,visited,prev):

            if r<0 or r>=rows or c<0 or c>=columns:
                return

            if (r,c) in visited or heights[r][c]<prev:
                return

            visited.add((r,c))
            h=heights[r][c]

            dfs(r+1,c,visited,h)   
            dfs(r-1,c,visited,h)   
            dfs(r,c+1,visited,h)   
            dfs(r,c-1,visited,h)        

        
        for c in range(columns):
            dfs(0, c, pac, heights[0][c])                
            dfs(rows - 1, c, atl, heights[rows - 1][c])   
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])                 
            dfs(r, columns - 1, atl, heights[r][columns - 1])   

        return [[r, c] for (r, c) in pac & atl]
        