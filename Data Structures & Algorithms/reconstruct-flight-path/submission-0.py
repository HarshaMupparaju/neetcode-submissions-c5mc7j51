class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets = sorted(tickets)

        adj_list = {}

        for s, d in tickets:
            if(s in adj_list):
                adj_list[s].append(d)
            else:
                adj_list[s] = [d]
        
        res = []
        res.append('JFK')

        def dfs(src):
            if(len(res) == len(tickets) + 1):
                return True
            
            if(src not in adj_list):
                return False
            
            temp = adj_list[src].copy()
            for i, node in enumerate(temp):
                adj_list[src].pop(i)
                res.append(node)
                
                if dfs(node):
                    return True
                adj_list[src].insert(i, node)
                res.pop()
            
            return False




        dfs('JFK')

        return res