# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float('-inf')

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res

            if(root == None):
                return -1e7
            
            left_max = dfs(root.left)
            right_max = dfs(root.right)


            res = max(root.val, left_max + root.val, right_max + root.val, left_max + right_max + root.val, res)
            print(res)

            return max(root.val, left_max + root.val, right_max + root.val)
            


        _ = dfs(root)

        return res