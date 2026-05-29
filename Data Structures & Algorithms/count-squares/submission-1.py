class CountSquares:

    def __init__(self):
        self.d_x = {}
        self.d_y = {}
        self.all_pts = {}

    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]

        if(x in self.d_x):
            self.d_x[x].append(point)
        else:
            self.d_x[x] = [point]
        
        if(y in self.d_y):
            self.d_y[y].append(point)
        else:
            self.d_y[y] = [point]
        
        if((x, y) in self.all_pts):
            self.all_pts[(x, y)] += 1
        else:
            self.all_pts[(x, y)] = 1
        
        return

    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]

        if(x not in self.d_x):
            return 0
        
        if(y not in self.d_y):
            return 0
        
        possible_x = self.d_x[x]
        possible_y = self.d_y[y]

        print(possible_x)
        print(possible_y)
        print(self.all_pts)

        res = 0

        for pos_x in possible_x:
            for pos_y in possible_y:
                print((pos_y[0], pos_x[1]) )
                if(pos_x == point or pos_y == point):
                    continue

                if((pos_y[0], pos_x[1]) in self.all_pts):
                    res += self.all_pts[(pos_y[0], pos_x[1])]
        
        return res


