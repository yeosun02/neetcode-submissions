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
    unordered_map<int, int> indices;
    int root_cntr = 0;
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); ++i) {
            indices[inorder[i]] = i;
        }
        return dfs(preorder, inorder, 0, inorder.size() - 1);
    }

    TreeNode* dfs(vector<int>& preorder, vector<int>& inorder, int l, int r) {
        if (l > r) {
            return nullptr;
        }
        TreeNode* root = new TreeNode(preorder[root_cntr]);
        int idx = indices[preorder[root_cntr++]];
        root->left = dfs(preorder, inorder, l, idx - 1);
        root->right = dfs(preorder, inorder, idx + 1, r);
        return root;
    }
};
