#include <cassert>

class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        if (right == left) {
            return right;
        }
        assert (right > left);
        int c = 0;
        while (right > left) {
            right = right >> 1;
            left = left >> 1;
            c++;
        }
        return left << c;
    }
};


/*
 * [1, 1, 0, 0, 1]
 * [0, 1, 0, 0, 1]
 * -> 
 * [0, 0, 0, 0, 0]
 *
 * [1, 1, 1, 0, 0]
 * [1, 1, 0, 0, 0]
 * ->
 * [1, 1, 0, 0, 0]
 *
 * return [1 if a_{bit}[i] == b_{bit}[i] else 0 for _ in range(n)]
*/
