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
    struct TreeNode *newTree = malloc(sizeof(struct TreeNode));
    newTree->val = root->val;
    newTree->left = invertTree(root->right);
    newTree->right = invertTree(root->left);
    return newTree;
}
