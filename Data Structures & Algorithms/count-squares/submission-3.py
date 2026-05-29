class CountSquares:

    def __init__(self):
        self.d_x = {}
        # self.d_y = {}
        self.all_pts = {}

    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]

        if(x in self.d_x):
            self.d_x[x].append(point)
        else:
            self.d_x[x] = [point]
        
        # if(y in self.d_y):
        #     self.d_y[y].append(point)
        # else:
        #     self.d_y[y] = [point]
        
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
        
        # if(y not in self.d_y):
        #     return 0
        
        possible_x = self.d_x[x]
        # possible_y = self.d_y[y]

        res = 0

        #O(n^2)
        # for pos_x in possible_x:
        #     for pos_y in possible_y:
        #         if(pos_x == point or pos_y == point):
        #             continue

        #         if((pos_y[0], pos_x[1]) in self.all_pts):
        #             res += self.all_pts[(pos_y[0], pos_x[1])]

        #O(n)
        for pos_x in possible_x:
            if(pos_x == point):
                continue

            side_length = abs(pos_x[1] - y)

            point1_a = (x + side_length, y)
            point1_b = (x - side_length, y)

            point2_a = (x + side_length, pos_x[1])
            point2_b = (x - side_length, pos_x[1])

            if(point1_a in self.all_pts and point2_a in self.all_pts):
                res += self.all_pts[point1_a] * self.all_pts[point2_a]
            
            if(point1_b in self.all_pts and point2_b in self.all_pts):
                res += self.all_pts[point1_b] * self.all_pts[point2_b]

        return res
