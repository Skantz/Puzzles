struct Node {
    int _;
    struct Node *left;
    struct Node *right;
};

int countNodes(struct Node* root) {
    if (!root) { 
        return 0;
    } 
    return 1 + countNodes(root->left) + countNodes(root->right);
}
