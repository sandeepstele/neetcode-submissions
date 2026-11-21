# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def dfs(node,miv,mav):

            if not node:
                return True
            
            if not miv<node.val<mav:
                return False
            
            left=dfs(node.left,miv,node.val)
            right=dfs(node.right,node.val,mav)

            return left and right

        
        return dfs(root,-9999999999999999999999,99999999999999999)
            



