#import <vector>
#import <math.h>

class Solution {
public:
    int maximumStrongPairXor(std::vector<int>& nums) {
        int maxx = 0;
        for (auto n1 : nums) {
            for (auto n2 : nums) {
                if (abs(n1 - n2) < std::min(n1, n2) + 1) {
                    maxx = std::max(maxx, n1 ^ n2);
                }
            }
        }
        return maxx;
    }
};
