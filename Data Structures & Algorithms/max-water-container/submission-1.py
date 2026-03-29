class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start_ptr = 0
        end_ptr = len(heights) - 1

        

        max_left_so_far = heights[0]

        max_right_so_far = heights[-1]

        max_area_so_far = min(max_left_so_far, max_right_so_far) * (len(heights) - 1)

        while(start_ptr < end_ptr):
            if(heights[start_ptr] <= heights[end_ptr]):
                start_ptr += 1
            else:
                end_ptr -= 1
            
            if(min(heights[start_ptr], heights[end_ptr]) * (end_ptr - start_ptr) > max_area_so_far):
                max_area_so_far = min(heights[start_ptr], heights[end_ptr]) * (end_ptr - start_ptr)
        
        return max_area_so_far
            