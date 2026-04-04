class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key in self.d):
            self.d[key].append([value, timestamp])
        else:
            self.d[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if(key in self.d):
            # res = self.d[key][-1][0]
            # Binary search
            start = 0
            end = len(self.d[key]) - 1

            temp = -1

            while(start <= end):
                mid = (start + end) // 2

                if(self.d[key][mid][1] <= timestamp):
                    start = mid + 1
                    temp = mid
                else:
                    end = mid - 1
            
            if(temp != -1):
                res = self.d[key][temp][0]
            else:
                res = ""

        else:
            res = ""
        
        return res
