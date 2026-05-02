class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key= lambda l:l[0])

        res = []
        hp = []
        i = 0
        time = 0
        n = len(tasks)

        while(i < n or hp):
            
            while(i< n and time >= tasks[i][0]):
                heapq.heappush(hp, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not hp:
                time = tasks[i][0]
            else:
                proc_time, index = heapq.heappop(hp)
                time += proc_time
                res.append(index)
        
        return res