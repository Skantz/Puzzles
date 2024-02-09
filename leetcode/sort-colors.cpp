class Solution {
public:
    void sortColors(vector<int>& nums) {
        int a = 0;
        int b = 0;
        int c = 0;
        for (auto e : nums) {
            if (e == 0) {
                a++;
            } else if (e == 1) {
                b++;
            } else {
                c++;
            }
        }
        for (int i = 0; i < nums.size(); i++) {
            if (i < a) {
                nums[i] = 0;
            } else if (i < a + b) {
                nums[i] = 1;
            } else {
                nums[i] = 2;
            }
        }
        return;
    }
};
