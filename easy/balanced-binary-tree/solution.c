/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct Result {
    bool balanced;
    int height;
};

#define MAX(x, y) ((x > y) ? x : y)

struct Result dfs(struct TreeNode* node) {
    if (!node) {
        struct Result empty = { .balanced = true, .height = 0 };
        return empty;
    }

    struct Result left = dfs(node->left);
    struct Result right = dfs(node->right);

    struct Result res = {
        .balanced = left.balanced &&
            right.balanced &&
            abs(left.height - right.height) <= 1,
        .height = 1 + MAX(left.height, right.height)
    };

    return res;
}

bool isBalanced(struct TreeNode* root) {
    return dfs(root).balanced;
}
