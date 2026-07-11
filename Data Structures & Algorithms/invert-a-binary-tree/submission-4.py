# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #TC: O(n) and SC: O(n); where n is the number of nodes in the tree
        def invert(node: Optional[TreeNode]) -> None:

            if(node == None):
                return

            node.left, node.right = node.right, node.left

            invert(node.left)
            invert(node.right)

            return

        invert(root)

        return root