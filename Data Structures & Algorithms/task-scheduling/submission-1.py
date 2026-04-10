class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Each task takes 1 unit of time
        #Have to greedily process tasks , always process the most frequent task

        hp = []

        d = {}

        for task in tasks:
            if(task in d):
                d[task] += 1
            else:
                d[task] = 1
        
        for k in d:
            heapq.heappush(hp, [-d[k], k]) #Pseudo max heap

        q = deque()
        cycle = 1

        while(len(hp) != 0 or len(q) != 0):
            if(len(hp) != 0):
                top = heapq.heappop(hp)
                print(top)
                print(cycle)
                
                if(top[0] + 1 != 0):
                    q.append([cycle + 1 + n, top[0] + 1, top[1]])


            while(len(q) != 0 and q[0][0] <= cycle + 1):
                front = q.popleft()
                heapq.heappush(hp, [front[1], front[2]])
            
            cycle += 1
    
        return cycle - 1

