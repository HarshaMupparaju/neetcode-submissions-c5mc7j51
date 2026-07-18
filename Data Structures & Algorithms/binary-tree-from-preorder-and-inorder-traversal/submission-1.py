# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if(len(preorder) == 0):
            return None
        
        node = TreeNode(preorder[0])

        inorder_idx = inorder.index(preorder[0])
        # for i in range(len(inorder)):
        #     if(inorder[i] == preorder[0]):
        #         inorder_idx = i
        #         break
        

        node.left = self.buildTree(preorder[1: inorder_idx + 1], inorder[:inorder_idx])

        node.right = self.buildTree(preorder[inorder_idx + 1: ], inorder[inorder_idx + 1: ]) 


        return node
