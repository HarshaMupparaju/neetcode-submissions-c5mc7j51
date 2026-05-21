class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int start = 0;
        int end = (int)prices.size() - 1;

        vector<int> prefix(prices.size(), 0);
        vector<int> suffix(prices.size(), 0);

        int temp = INT_MAX;
        for(int i=0;i<prices.size();i++) {
            temp = min(prices[i], temp);
            prefix[i] = temp;
        }

        temp = INT_MIN;
        for(int i = prices.size() - 1;i >= 0; i--) {
            temp = max(prices[i], temp);
            suffix[i] = temp;
        }

        int res = 0;
        for(int i=0;i < prices.size(); i++) {
            res = max(res, suffix[i] - prefix[i]);
        }
        return res;

    }
};
