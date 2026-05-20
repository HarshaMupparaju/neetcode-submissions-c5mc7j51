class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        bool res = false;

        unordered_set<int> s;

        for(int i = 0; i < (int)nums.size(); i ++) {
            if(s.count(nums[i]) > 0) {
                // nums[i] is already in s
                res = true;
                break;
            }
            else {
                s.insert(nums[i]);
            }
        }

        return res;
    }
};