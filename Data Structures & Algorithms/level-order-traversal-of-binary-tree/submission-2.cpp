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
        if (!root) return {};
        vector<vector<int>> res;
        queue<pair<TreeNode*, int>> que;
        que.push({root, 0});

        while (!que.empty()) {
            auto [node, level] = que.front();
            que.pop();
            if (res.size() <= level) { 
                res.push_back({});
            }
            res[level].push_back(node->val);
            if (node->left) que.push({node->left, level + 1});
            if (node->right) que.push({node->right, level + 1});
        }

        return res;
    }
};
