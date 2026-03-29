# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]

        def dfs(root: Optional[TreeNode], count: List[int], k: int):
            if(root == None):
                return None

            left = dfs(root.left, count, k)
            if(left):
                return left
            
            count[0] += 1
            print(count)
            if(count[0] == k):
                # print('####')
                return root.val

            right = dfs(root.right, count, k)
            if(right):
                return right

            return None

        return dfs(root, count, k)

        