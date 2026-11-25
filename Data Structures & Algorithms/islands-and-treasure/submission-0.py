from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q=deque()
        INF = 2147483647

        rows,columns=len(grid),len(grid[0])

        d=[(1,0),(-1,0),(0,1),(0,-1)]


        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==0:
                    q.append((r,c))
        

        while q:
                r,c =q.popleft()
                for dr,dc in d:

                    nr,nc = r+dr,c+dc

                    if 0<= nr < rows and 0<= nc< columns and grid[nr][nc]==INF:
                        grid[nr][nc]=grid[r][c]+1
                        q.append((nr,nc))
        

            








            