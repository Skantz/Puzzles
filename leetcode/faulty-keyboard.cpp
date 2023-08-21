class Solution {
public:
    string finalString(string s) {
        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            if (c == 'i') {
                std::reverse(s.begin(), s.begin() + i); 
            }
        }
        auto f = [&s](const char& c) { return c == 'i'; };
        s.erase(std::remove_if(s.begin(), s.end(), f), s.end());
        return s;
    }
};
