/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* invertTree(struct TreeNode* root) {
    if (!root)
        return NULL;
    struct TreeNode* left = invertTree(root->right);
    struct TreeNode* right = invertTree(root->left);
    root->left = left;
    root->right = right;
    return root;
}
