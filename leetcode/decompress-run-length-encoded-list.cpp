#include <vector>

using std::vector;

class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> outs;
        for (unsigned long i = 0; i < nums.size() / 2; i++) {
            int f = nums[2 * i];
            int e = nums[2* i + 1];
            for (int j = 0; j < f; j++) {
                outs.push_back(e);
            }
        }
        return outs;
    }
};
