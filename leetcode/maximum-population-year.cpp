class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        int N = logs.size();
        int counts[2050 - 1950 + 1] = { 0 };
        for (auto tup : logs) {
            int s = tup[0];
            int e = tup[1];
            for (int i = 0; i < e - s; i++) {
                counts[s - 1950 + i] = counts[s - 1950 + i] + 1;
            }
        }
        for (auto e : counts) {
            cout << e << ";";
        }
        int* r = std::max_element(std::begin(counts), std::end(counts));
        return 1950 + std::distance(std::begin(counts), r);
    }
};
