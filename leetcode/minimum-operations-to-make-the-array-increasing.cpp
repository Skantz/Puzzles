class Solution {
  public:
    int minOperations(vector<int> nums){
        int sum = 0;
        int i = 1;
        std::for_each(std::begin(nums) + 1,
                      std::end(nums),
                      [&nums, &sum, &i](int v)
                      { sum += std::max(0, nums[i - 1] - v + 1);
                        nums[i] = std::max(nums[i], nums[i - 1] + 1);
                        i++;
                      });
        return sum;
    }
};
