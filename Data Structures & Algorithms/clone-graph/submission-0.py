"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        
        l={}

        def dfs(n):
            if n in l:
                return l[n]
            
            copy=Node(n.val)
            l[n]=copy

            for i in n.neighbors:
                copy.neighbors.append(dfs(i))

            return copy

        return dfs(node)

        