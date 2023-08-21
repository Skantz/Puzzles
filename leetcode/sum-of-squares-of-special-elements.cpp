class Solution {
public:
    int sumOfSquares(vector<int> nums) {
        int s = 0, i = 1, n = nums.size();
        for (auto e : nums) {
            s += (n % i) == 0 ? nums[i - 1] * nums[i - 1] : 0;
            i++;
        }
        return s;
    }
};
