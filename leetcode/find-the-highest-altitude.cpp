class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        vector<int> res(gain.size());
        auto t = std::partial_sum(gain.begin(), gain.end(), res.begin(), plus<int>());
        return std::max(0, *max_element(res.begin(), res.end()));
    }
};
