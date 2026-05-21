class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;

        unordered_map<int, int> mp;

        priority_queue<pair<int, int>> pq;

        for(int i = 0; i < nums.size(); i++) {
            if(mp.contains(nums[i])) {
                mp[nums[i]] += 1;
            }
            else {
                mp[nums[i]] = 1;
            }
        }

        for(auto& [key, value]: mp) {
            pq.push({value, key});
        }

        for(int i = 0; i< k; i++) {
            res.push_back(pq.top().second);
            pq.pop();
        }

        return res;
    }
};
