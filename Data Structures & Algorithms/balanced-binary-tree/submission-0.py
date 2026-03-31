# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root: Optional[TreeNode]) -> int:
            if(root == None):
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
        
            if(left == -1 or right == -1):
                return -1

            if(abs(left - right) > 1):
                res = -1
            else:
                res = max(left, right) + 1
            
            return res

        res = dfs(root)
        if(res == -1):
            return False
        
        return True