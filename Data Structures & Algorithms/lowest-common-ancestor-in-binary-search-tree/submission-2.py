# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)

            if(node.val == p.val or node.val == q.val):
                # if(left != None or right != None):
                return node
            else:
                if(left == None and right == None):
                    return None
                
                if(left == None):
                    return right
                
                if(right == None):
                    return left
                
                if(left != None and right != None):
                    return node


        res = dfs(root)

        return res