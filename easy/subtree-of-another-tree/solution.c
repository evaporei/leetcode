/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool sameTree(struct TreeNode* p, struct TreeNode* q) {
    if (!p && !q)
        return true;
    if (!p || !q)
        return false;
    return p->val == q->val && sameTree(p->left, q->left) && sameTree(p->right, q->right);
}

bool dfs(struct TreeNode* node, struct TreeNode* subRoot) {
    if (!node)
        return false;

    return sameTree(node, subRoot) ||
        dfs(node->left, subRoot) ||
        dfs(node->right, subRoot);
}

bool isSubtree(struct TreeNode* root, struct TreeNode* subRoot) {
    return dfs(root, subRoot);
}
