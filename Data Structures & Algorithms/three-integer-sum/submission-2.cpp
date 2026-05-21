class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        vector<vector<int>> res;
        set<vector<int>> st;

        
        for(int i = 0; i< nums.size(); i++) {
            for(int j =  i + 1; j < nums.size(); j++) {
                for(int k = j + 1; k < nums.size(); k++) {
                    if(i != j && i != k && j != k) {
                        if(nums[i] + nums[j] + nums[k] == 0) {
                            vector<int> triplet = {nums[i], nums[j], nums[k]};
                            vector<int> sorted_triplet = triplet;
                            sort(sorted_triplet.begin(), sorted_triplet.end());
                            if(!(st.contains(sorted_triplet))) {
                                res.push_back(triplet);
                                sort(triplet.begin(), triplet.end());
                                st.insert(triplet);
                            }
                            
                        }
                    }
                }
            }
        }

        return res;
    }
};
