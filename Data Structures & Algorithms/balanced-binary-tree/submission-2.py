# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #TC: O(n), SC: O(n), where n is the number of nodes
        res = [True]
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if(abs(right - left) > 1):
                res[0] = False
            
            return 1 + max(left, right)

        _ = dfs(root)

        return res[0]