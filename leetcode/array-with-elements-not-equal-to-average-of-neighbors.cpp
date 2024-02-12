#include <vector>
#include <algorithm>

using std::vector;

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<int> ret;
        int n = nums.size();
        sort(nums.begin(), nums.end()); // n * log(n)
        for (int i = 0; i < n/2; i++) {
            ret.push_back(nums[i]);
            ret.push_back(nums[n - i - 1]);
        }
        if (n % 2) {
            ret.push_back(nums[n - n/2 - 1]);
        }
        return ret;
    }
};

/* O(n) possible. */
