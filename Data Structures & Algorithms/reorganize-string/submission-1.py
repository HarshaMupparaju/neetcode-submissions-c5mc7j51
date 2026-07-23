class Solution:
    def reorganizeString(self, s: str) -> str:
        
        d = {}
        for c in s:
            if(c in d):
                d[c] += 1
            else:
                d[c] = 1
        
        res =[]
        hp = []
        for key in d:
            heapq.heappush(hp, [-d[key], key])

        

        while(len(res) != len(s)):
            # print(hp)
            freq, ele = heapq.heappop(hp)
            # print(hp)
            if(len(res) == 0):
                res.append(ele)
                if(freq + 1 < 0):
                    heapq.heappush(hp, [freq + 1, ele])
                continue

            if(ele != res[-1]):
                res.append(ele)
                if(freq + 1 < 0):
                    heapq.heappush(hp, [freq + 1, ele])
            else:
                if(len(hp) == 0):
                    return '' #impossible
                else:
                    freq2, ele2 = heapq.heappop(hp)
                    res.append(ele2)
                    if(freq2 + 1 < 0):
                        heapq.heappush(hp, [freq2 + 1, ele2])
                    heapq.heappush(hp, [freq, ele])


        return ''.join(res)