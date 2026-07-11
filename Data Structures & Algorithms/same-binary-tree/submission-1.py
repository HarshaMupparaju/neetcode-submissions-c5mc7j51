# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if(node1 == None and node2 == None):
                return True
            
            if(node1 == None or node2 == None):
                return False


            if(node1.val != node2.val):
                return False

            left = dfs(node1.left , node2.left)
            right = dfs(node1.right, node2.right)

            return left and right

        res = dfs(p, q)

        return res