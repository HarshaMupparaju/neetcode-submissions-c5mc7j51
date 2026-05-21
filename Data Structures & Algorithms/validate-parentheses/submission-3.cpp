class Solution {
public:
    bool isValid(string s) {
        bool res = true;
        stack<int> stk;

        for(int i=0;i<s.size();i++) {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
                stk.push(s[i]);
            }
            else {
                if(stk.size() == 0) {
                    res = false;
                    break;
                }
                char top = stk.top();
                if(s[i] == ')' && top != '(') {
                    res = false;
                    break;
                }
                else if(s[i] == '}' && top != '{') {
                    res = false;
                    break;
                }
                else if(s[i] == ']' && top != '[') {
                    res = false;
                    break;
                }
                stk.pop();
            }
        }
        if(stk.size() != 0){
            res = false;
        }

        return res;
    }
};
