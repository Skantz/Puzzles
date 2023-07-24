class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 2) {return nums.size(); }
        int c = 2;
        for (size_t i = 2; i < nums.size(); i++) {
            if (nums[i - 2] == nums[i]) {i--; nums.erase(nums.begin() + i); }
            else {c++; }
        }
        return c;
    }
};
