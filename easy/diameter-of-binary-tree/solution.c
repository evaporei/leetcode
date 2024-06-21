/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct Diameter {
    int curr;
    int max;
};

#define MAX(x, y) ((x > y) ? x : y)

struct Diameter dfs(struct TreeNode* node) {
    if (!node) {
        struct Diameter none = { .curr = 0, .max = 0 };
        return none;
    }
    
    struct Diameter left = dfs(node->left);
    struct Diameter right = dfs(node->right);

    int curr = 1 + MAX(left.curr, right.curr);
    int max = MAX(MAX(left.max, right.max), left.curr + right.curr);

    struct Diameter res = {
        .curr = curr,
        .max = max
    };

    return res;
}

int diameterOfBinaryTree(struct TreeNode* root) {
    return dfs(root).max;
}
