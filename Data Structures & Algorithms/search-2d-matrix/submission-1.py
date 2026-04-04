class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)

        n = len(matrix[0])

        start = [0, 0]

        end = [m - 1, n - 1]

        while(start[0] * n + start[1] <= end[0] * n + end[1]):
            start_unrolled = start[0] * n + start[1] 
            end_unrolled = end[0] * n + end[1]
            mid_unrolled = (start_unrolled + end_unrolled) // 2
            mid = [mid_unrolled // n, mid_unrolled % n ]
            # mid = [(start[0] + end[0])// 2, (start[1] + end[1])// 2]
            # print(mid)
            if(matrix[mid[0]][mid[1]] == target):
                return True
            elif(matrix[mid[0]][mid[1]] < target):
                if(mid[1] + 1 == n):
                    start = [mid[0] + 1, 0] #move down a row
                else:
                    start = [mid[0], mid[1] + 1]
            else:
                if(mid[1] - 1 == -1):
                    end = [mid[0] - 1, n - 1] #move up a row
                else:
                    end = [mid[0], mid[1] - 1]
            print(f'start:{start}, mid:{mid}, end: {end}')
        return False