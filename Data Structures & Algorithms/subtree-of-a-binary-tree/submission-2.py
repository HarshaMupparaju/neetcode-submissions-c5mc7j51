# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = [False]

        def check_subtree(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if(node1 == None and node2 == None):
                return True
            
            if(node1 == None or node2 == None):
                return False
            
            if(node1.val != node2.val):
                return False
            
            left = check_subtree(node1.left, node2.left)
            right = check_subtree(node1.right, node2.right)

            return left and right

        def dfs(node: Optional[TreeNode]) -> None:
            if(node == None):
                return 
            
            if node.val == subRoot.val :
                res[0] = check_subtree(node, subRoot)
            
            if(res[0] == True):
                return
            
            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)

        return res[0]