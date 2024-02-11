#include <algorithm>
#include <climits>
#include <set>
#include <vector>

using std::set;
using std::vector;

/* remove */
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
};
/* remove */

class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        if (root == nullptr) {
            return vector<int>{};
        }
        vector<int> ret;
        set<TreeNode*> q;
        q.insert(root);
        while (!q.empty()) {
            vector<TreeNode*> r(q.begin(), q.end());
            q.clear();
            int maxx = INT_MIN;
            for (TreeNode* e : r) {
                if (e->left != nullptr) {
                    q.insert(e->left);
                }
                if (e->right != nullptr) {
                    q.insert(e->right);
                }
                if (maxx < e->val) {
                    maxx = e->val;
                }
            }
            ret.push_back(maxx);
        }
        return ret;
    }
};
