class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = (int)heights.size() - 1;

        int res = INT_MIN;

        while(left < right) {
            res = max(res, min(heights[left], heights[right]) * (right - left));

            if(heights[left] <= heights[right]) {
                left += 1;
            }
            else {
                right -= 1;
            }
        }

        return res;
    }
};
