# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxd=0
        def gh(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh =gh(node.left)
            rh =gh(node.right)

            self.maxd=max(self.maxd,lh+rh)

            return 1+max(lh,rh)
        gh(root)
        return self.maxd
        

        