class Solution {
public:
    bool isPrefixString(string s, vector<string>& words) {
        string s_ = "";
        for (string e : words) {
            s_ = s_ + e;
            if (s == s_) {
                return true;
            }
        }
        return false;
    }
};
