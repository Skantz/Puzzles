#include <vector>

using std::vector;

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> ret;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int e = nums[i];
            for (int j = 0; j < n; j++) {
                int ep = nums[(i + 1 + j) % n];
                if (e < ep) {
                    ret.push_back(ep);
                    break;
                }
                if (j == n - 1) {
                    ret.push_back(-1);
                }
            }
        }
        return ret;
    }
};
