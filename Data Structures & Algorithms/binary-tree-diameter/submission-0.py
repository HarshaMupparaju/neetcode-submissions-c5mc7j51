# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = -1e7
    
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res

            if(node == None):
                return -1

            left = dfs(node.left)

            right = dfs(node.right)

            print(f"left:{left}, right: {right}")

            res = max(res, left + 1, right + 1, left + 1 + right + 1)
            print(res)

            return max(left + 1, right + 1)

        _ = dfs(root)

        return res