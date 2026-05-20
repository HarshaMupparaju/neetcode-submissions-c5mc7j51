class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;

        unordered_map<string, vector<string>> mp;

        for(int i=0; i < strs.size(); i++) {
            string temp = strs[i];
            sort(temp.begin(), temp.end());

            if(mp.contains(temp)) {
                mp[temp].push_back(strs[i]);
            }
            else {
                mp[temp] = {strs[i]};
            }
        }

        for(auto i=mp.begin(); i != mp.end(); i++) {
            res.push_back(i->second);
        }

        return res;
    }
};
