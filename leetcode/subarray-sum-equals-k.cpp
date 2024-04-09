#include <vector>

using std::vector;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        vector<int> runsum;
        int s = 0;
        runsum.push_back(0);
        for (auto e: nums) {
            s += e;
            runsum.push_back(s);
        }
        int ret = 0;
        /* improve : 1 pass */
        for (unsigned int i = 0; i < runsum.size(); i++) {
            for (unsigned int j = i + 1; j < runsum.size(); j++) {
                if ((runsum[j] - runsum[i]) == k) {
                    ret++;
                }
            }
        }
        return ret;
    }
};
