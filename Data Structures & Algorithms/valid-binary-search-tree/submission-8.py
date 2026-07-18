# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode], l, r) -> bool:
            if not node:
                return True
            
            if(node.val <= l or node.val >= r):
                return False
            
            left = dfs(node.left, l, node.val)
            right = dfs(node.right, node.val, r)

            return left and right
            

        res = dfs(root, float('-inf'), float('inf'))

        return res