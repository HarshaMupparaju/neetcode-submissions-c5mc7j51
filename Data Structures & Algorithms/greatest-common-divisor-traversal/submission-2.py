class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        adj_list = {i: [] for i in range(len(nums))} #undirected graph
        reachable_nodes = {}

        #make adjacency list
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(math.gcd(nums[i], nums[j]) > 1):
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        

        def dfs(node: int) -> None:
            if(node in vis):
                return
            
            vis.add(node)
            if(node in reachable_nodes):
                vis.update(reachable_nodes[node])
                return

            for nei in adj_list[node]:
                dfs(nei)
            
            return


        #Traverse the graph from each node and store reachable nodes
        for i in range(len(nums)):
            vis = set()
            dfs(i)
            reachable_nodes[i] = vis

        #Verify all the pairs consisting that node are reachable in its nodes, if we have extra that's ok
        for i in range(len(nums)):
            reachable = reachable_nodes[i]
            for j in range(i + 1, len(nums)):
                if(j not in reachable):
                    return False

        #Return
        return True