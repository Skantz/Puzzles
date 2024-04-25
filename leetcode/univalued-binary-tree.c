#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *l;
    struct TreeNode *r;
};

bool isUnivalTree(struct TreeNode* root) {
    if (!root) {
        return true;
    }
    return (!root->l  || (root->val == root->l->val)) &&
           (!root->r || (root->val == root->r->val)) &&
           isUnivalTree(root->l) &&
           isUnivalTree(root->r);
}
