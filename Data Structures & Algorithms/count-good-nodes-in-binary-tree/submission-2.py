# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node: Optional, max_val: int) -> None:
            nonlocal res

            if not node:
                return None
            
            if(node.val >= max_val):
                res += 1
            
            dfs(node.left, max(max_val, node.val))
            dfs(node.right, max(max_val, node.val))

            return

        dfs(root, float('-inf'))

        return res