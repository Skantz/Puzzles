#include <vector>

class Solution {
public:
    std::vector<int> findArray(std::vector<int>& pref) {
        std::vector<int> ret;
        ret.push_back(pref[0]);
        int product = ret[0];
        for (unsigned int i = 1; i < pref.size(); i++) {
            ret.push_back(product ^ pref[i]);
            product ^= ret[i];
        }
        return ret;
    }
};
