#include <string>
#include <vector>
#include <algorithm>

using std::string;
using std::vector;

class Solution {
public:
    int maxVowels(string s, int k) {
    
        int sz = s.size();
    
        std::vector<int> vowel {(int)'a', (int)'e', (int)'i', (int)'o', (int) 'u'};
        auto is_vowel = [vowel](char x) { return std::find(vowel.begin(), vowel.end(), x) != vowel.end(); };

        int sum = 0;
        for (int i = 0; i < k; i++) {
            if (is_vowel(s[i])) {
                sum += 1;
            }
        }

        int maxx = sum;

        for (int i = 1; i < sz - k + 1; i++) {
            if (is_vowel(s[i - 1])) {
                sum -= 1;
            }
            if (is_vowel(s[i + k - 1])) {
                sum += 1;
            }
            if (sum > maxx) {
                maxx = sum;
            }
        }
        return maxx;
    }
};
