#include <vector>
#include <unordered_map>
#include <algorithm>

using std::pair;
using std::vector;
using std::unordered_map;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        unordered_map<int, vector<pair<int, int>>> map_;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int x = nums[i];
                int y = nums[j];
                if (map_.find(x + y) == map_.end()) {
                    pair<int, int> p = {i, j}; 
                    vector<pair<int, int>> v = {p};
                    map_[x + y] = v;
                } else {
                    map_[x + y].push_back(pair<int, int>(i, j));
                }
            }
        }
        vector<int> possible_values; // c++ slow map key iteration
        for (auto s : map_) {
            int t = s.first;
            possible_values.push_back(t);
        }
        int min = 10001 * 3;
        int x, y, z;
        for (int k = 0; k < n; k++) {
            int c = nums[k];
            for (auto s : possible_values) {
                int ab = abs(c + s - target);
                if (ab < min) {
                    for (pair<int, int> p: map_[s]) {
                        if (p.first != k && p.second != k) {
                            min = ab;
                            x = nums[p.first];
                            y = nums[p.second];
                            z = c;
                            break;
                        }
                    }
                }
            }
        }
        return x + y + z;
    }
};
