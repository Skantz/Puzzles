class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        while (true) {
            auto eq = [&original](int x) { return x == original; };
            auto idx = std::find_if(nums.begin(), nums.end(), eq);
            if (idx == nums.end()) {
                break;
            }
            original = original * 2;
        }
        return original;
    }
};
