class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        // vector<int> output;

        // for(int i=0;i<nums.size(); i++) {
        //     int temp = 1;
        //     for(int j = 0; j<nums.size(); j ++) {
        //         if(i != j) {
        //             temp = temp * nums[j];
        //         }
        //     }
        //     output.push_back(temp);
        // }

        // return output;

        vector<int> output;

        long long temp = 1;
        int zeros = 0;

        for(int i=0;i < nums.size(); i++) {
            if(nums[i] != 0) {
                temp = temp * nums[i];
            }
            else {
                zeros = zeros + 1;
            }
            
        }

        for(int i=0; i< nums.size(); i++) {
            if(nums[i] == 0 && zeros <= 1) {
                output.push_back(temp);
            }
            else if (nums[i] == 0 && zeros > 1) {
                output.push_back(0);
            }
            else if(nums[i] != 0 && zeros == 0) {
                output.push_back(temp / nums[i]);
            }
            else {
                output.push_back(0);
            }
            
        }

        return output;
    }
};
