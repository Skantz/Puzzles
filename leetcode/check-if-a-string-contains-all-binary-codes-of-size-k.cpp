#include <string>
#include <set>

using std::string;
using std::set;

class Solution {
public:
    bool hasAllCodes(string s, int k) {
        // 2**20 ~ 10**6
        std::set<string> set_;
        int n = s.size();
        for (int i = 0; i < n - k + 1; i++) {
            string ss = s.substr(i, k); // (start, offset)
            set_.insert(ss);
        }
        return (set_.size() == (1 << k));
    }
};
