class Solution {
public:
    int maximum69Number (int num) {
        std::string s = std::to_string(num);
        int i = 0;
        for (auto e : s) {
            if (e == '6') {
                s[i] = '9';
                break;
            }
            i++;
        }
        int ret;
        std::from_chars(s.data(), s.data()+s.size(), ret);
        return ret;
    }
};
