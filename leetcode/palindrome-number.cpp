#include <algorithm>
#include <string>

class Solution {
public:
    bool isPalindrome(int x) {
        std::string x_ = std::to_string(x);
        std::reverse(x_.begin(), x_.end());
        return (std::to_string(x) == x_);
    }
};
