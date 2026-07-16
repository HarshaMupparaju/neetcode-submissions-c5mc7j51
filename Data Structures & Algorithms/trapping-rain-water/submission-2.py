class Solution:
    def trap(self, height: List[int]) -> int:
        left_highest = []
        right_highest = []

        current_max = 0
        for i in range(len(height)):
            left_highest.append(current_max)
            current_max = max(current_max, height[i])
        
        current_max = 0

        for i in range(len(height) - 1, -1, -1):
            right_highest.append(current_max)
            current_max = max(current_max, height[i])
        
        right_highest.reverse()
        
        print(left_highest)
        print(right_highest)
    
        res = 0

        for i in range(len(height)):
            if(min(left_highest[i], right_highest[i]) - height[i] >= 0):
                res += min(left_highest[i], right_highest[i]) - height[i]

        return res