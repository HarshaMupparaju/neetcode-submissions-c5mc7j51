class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;

        unordered_map<int, int> mp;

        for(int i=0; i < nums.size(); i++) {
            int b = target - nums[i];
            if(mp.count(b) == 1) {
                res.push_back(mp[b]);
                res.push_back((i));
                return res;
            }
            mp[nums[i]] = i;
        }
        return {-1, -1};
    }
};
