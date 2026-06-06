class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = {}

        tickets.sort()

        for src, dst in tickets:
            if(src in adj_list):
                adj_list[src].append(dst)
            else:
                adj_list[src] = [dst]
        
        res = ["JFK"]

        def dfs(node: str) -> None:
            if(len(res) == len(tickets) + 1):
                return True
            
            if(node not in adj_list): #No tickets from this location
                return False
            
            temp = list(adj_list[node])
            for i, v in enumerate(temp):
                #Use ticket
                
                adj_list[node].pop(i)
                res.append(v)

                if(dfs(v) == True):
                    return True
                
                adj_list[node].insert(i, v)
                res.pop()
            
            return False

        dfs('JFK')

        return res