class Solution:
    def trap(self, height: List[int]) -> int:
        
        ##O(n) TC and O(n) SC
        max_left = []
        max_right = []

        temp = 0
        for i in range(len(height)):
            max_left.append(temp)
            temp = max(temp, height[i])

        temp = 0

        for i in range(len(height) - 1, -1, -1):
            max_right.append(temp)
            temp = max(temp, height[i])
        
        max_right.reverse()

        res = 0

        print(max_left)
        print(max_right)

        for i in range(len(height)):
            temp = min(max_left[i], max_right[i]) - height[i]
            if(temp > 0):
                res += temp
                print(temp)


        return res