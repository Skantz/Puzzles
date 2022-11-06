class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 1) {return 0; }
        int c = 1;
        for (size_t i = 1; i < nums.size(); i++) {
            if (nums[i - 1] == nums[i]) {i--; nums.erase(nums.begin() + i); }
            else {c++; }
        }
        return c;
    }
};
