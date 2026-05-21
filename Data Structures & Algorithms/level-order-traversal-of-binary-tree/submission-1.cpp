/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;

        queue<TreeNode*> q;

        if(root == nullptr) {
            return res;
        }

        q.push(root);

        while(q.size() != 0) {
            int n = q.size();
            int count = 0;
            vector<int> temp;

            while(count < n) {
                TreeNode* front = q.front();
                if(front-> left != nullptr) {
                    q.push(front->left);
                }
                
                if(front->right != nullptr) {
                    q.push(front->right);
                }

                temp.push_back(front->val);

                q.pop();
                count = count + 1;
            }
            res.push_back(temp);
        }

        return res;
    }
};
