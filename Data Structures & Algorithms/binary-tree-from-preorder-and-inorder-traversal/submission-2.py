# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx


        preorder = iter(preorder)


        def helper(left,right):
            if left>right:
                return None
            

            val=next(preorder)
            mid= inorder_map[val]
            return TreeNode(val, helper(left, mid - 1), helper(mid + 1, right))
        return helper(0,len(inorder)-1)


