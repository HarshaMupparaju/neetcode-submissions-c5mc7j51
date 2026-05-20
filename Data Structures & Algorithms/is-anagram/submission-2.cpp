class Solution {
public:
    bool isAnagram(string s, string t) {
        bool res = true;

        unordered_map<char, int> st;

        if(s.size() != t.size()) {
            res = false;
            return res;
        }

        for(int i = 0; i < (int)s.size(); i ++) {
            st[s[i]] += 1;
        }

        for(int i=0; i < (int)t.size(); i ++) {
            if(st.count(t[i]) > 0 and st[t[i]] > 0) {
                st[t[i]] -= 1;
            }
            else {
                res = false;
                break;
            }
        }

        return res;
    }
};
