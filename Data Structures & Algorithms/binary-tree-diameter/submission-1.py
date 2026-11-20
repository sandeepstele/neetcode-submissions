# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            # 2. Base case: what should an empty node return?
            if not node:
                return 0
            
            # 3. Recursively find the height of the left and right subtrees

            left=dfs(node.left)
            right=dfs(node.right)

            
            # 4. Update self.res using the left and right heights

            self.res=max(self.res,right+left)
            
            # 5. Return the height of the current node to its parent
            return 1+ max(left,right)
            
        dfs(root)
        return self.res
      