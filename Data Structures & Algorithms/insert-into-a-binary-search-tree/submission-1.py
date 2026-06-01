# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            new_node = TreeNode(val)

            return new_node

        def dfs(node: Optional[TreeNode]):

            if(val < node.val):
                if(node.left):
                    dfs(node.left)
                else:
                    new_node = TreeNode(val)
                    node.left = new_node
                    return
            else:
                if(node.right):
                    dfs(node.right)
                else:
                    new_node = TreeNode(val)
                    node.right = new_node
                    return
            
            return

        dfs(root)

        return root