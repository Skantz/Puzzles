class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        int s = 0;
        words1.insert(words1.end(), words2.begin(), words2.end());
        for (string e : words2) {
            int c1 = count(words1.begin(), words1.end(), e);
            int c2 = count(words2.begin(), words2.end(), e);
            s = s + ((c1 == 2) ? (c2 == 1) ? 1 : 0 : 0);
        }
        return s;
    }
};
