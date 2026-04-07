# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        hp = []

        res = 0

        heapq.heappush(hp, (float('inf'), 1))

        def dfs(node: TreeNode) -> None:
            nonlocal res

            if not node:
                return
            
            if(-hp[0][0] <= node.val):
                res += 1
                print(node.val)
                heapq.heappush(hp, (-node.val, 1))

            dfs(node.left)
            dfs(node.right)

            if(-hp[0][0] == node.val):
                heapq.heappop(hp)

            return

        dfs(root)

        return res