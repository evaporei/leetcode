/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define MAX(x, y) ((x > y) ? x : y)
int maxDepth(struct TreeNode* root) {
    if (!root)
        return 0;
    if (!root->left && !root->right)
        return 1;
    int left = 1 + maxDepth(root->left);
    int right = 1 + maxDepth(root->right);
    return MAX(left, right);
}
