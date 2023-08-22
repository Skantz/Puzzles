class Solution {
public:
    int findLucky(vector<int>& arr) {
        int maxx = -1;
        for (auto e : arr) {
            int c = count(arr.begin(), arr.end(), e);
            if (c == e) {
                maxx = max(c, maxx);
            }
        }
        return maxx >= 0 ? maxx : -1;
    }
};
