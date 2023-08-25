class Solution {
public:
    bool isThree(int n) {
        int d = 1;
        for (int i = 1; i < n; i++) {
            if ((n % i) == 0) {
                d += 1;
            }
        }
        if (d == 3) {
            return true;
        }
        return false;
    }
};
