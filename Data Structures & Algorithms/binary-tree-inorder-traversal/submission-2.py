# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # #Recursive solution
        # def dfs(node: Optional[TreeNode]) -> None:
        #     if(node == None):
        #         return
            
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)

        #     return 

        # dfs(root)

        #Iterative solution
        st = []
        cur = root
        
        while(cur or st):
            while(cur):
                st.append(cur)
                cur = cur.left
            
            cur = st.pop()
            res.append(cur.val)

            cur = cur.right

        return res