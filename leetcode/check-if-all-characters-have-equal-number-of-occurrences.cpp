class Solution {
public:
    bool areOccurrencesEqual(string s) {
        std::unordered_map<char, size_t> cs;
        for (auto e : s) {
            ++cs[e];
        }
        std::unordered_map<size_t, size_t> cs_;
        for (auto e : cs) {
            size_t e_ = e.second;
            ++cs_[e_];
        }
        return cs_.size() == 1;
    }
};
