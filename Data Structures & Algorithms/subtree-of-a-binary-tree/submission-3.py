# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_same_tree(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if(node1 == None and node2 == None):
                return True
            
            if(node1 == None or node2 == None):
                return False
            
            if(node1.val != node2.val):
                return False
            
            left = check_same_tree(node1.left, node2.left)
            right = check_same_tree(node1.right, node2.right)

            return left and right

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            
            if(node.val == subRoot.val):
                if(check_same_tree(node, subRoot)):
                    return True
            
            left = dfs(node.left)
            right = dfs(node.right)

            return left or right

        res = dfs(root)

        return res