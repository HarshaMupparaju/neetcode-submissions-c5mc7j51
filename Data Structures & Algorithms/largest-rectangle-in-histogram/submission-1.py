class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        st = []

        max_area = -1

        for i in range(len(heights)):
            if(len(st) == 0):
                st.append([i, heights[i]])
                continue
            
            start = i

            while(len(st) > 0 and heights[i] < st[-1][1]):
                max_area = max(max_area, st[-1][1] * (i - st[-1][0]))
                start = st[-1][0] # Track till where the current bar can be extended back
                st.pop()

            st.append([start, heights[i]])
        
        #Process the remaining elements in the stack
        while(st):
            max_area = max(max_area, st[-1][1] * (len(heights) - st[-1][0]))
            st.pop()
        
        return max_area
