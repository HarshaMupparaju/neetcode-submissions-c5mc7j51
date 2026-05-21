class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0;
        int end = s.size() - 1;

        bool res = true;

        while( start <= end) {
            while(start < end && !isalnum(s[start])) {
                start += 1;
            }

            while(start < end && !isalnum(s[end])) {
                // cout << s[end];
                // cout << (s[end] >= 'a' && s[end] <= 'z');
                end -= 1;
            }
            // cout << start << end;
            if(tolower(s[start]) != tolower(s[end])) {
                cout << s[start] << s[end];
                res = false;
                break;
            }

            start += 1;
            end -= 1;
        }

        return res;
    }
};
