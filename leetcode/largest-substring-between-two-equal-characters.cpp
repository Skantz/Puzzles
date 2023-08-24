class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int maxx = -1;
        for (auto e : s) {
            int c = std::count(s.cbegin(), s.cend(), e);
            if (c > 1) {
                int fst = s.find(e);
                int snd = s.rfind(e);
                maxx = max(snd - fst - 1, maxx);
            }
        }
        return maxx;
    }
};
