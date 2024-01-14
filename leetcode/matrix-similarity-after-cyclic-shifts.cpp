#include <vector>

class Solution {
public:
    bool areSimilar(std::vector<std::vector<int>>& mat, int k) {
        for (int i = 0; i < mat.size(); i++) {
            for (int j = 0; j < mat[0].size(); j++) {
                if (mat[i][j] != mat[i][(j + k) % (mat[0].size())]) {
                    return false;
                }
            }
        }
        return true;
    }
};
