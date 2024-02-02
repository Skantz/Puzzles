int max2(int x, int y) {
    if (x < y) {
        return y;
    }
    return x;
}

int min2(int x, int y) {
    if (max2(x, y) == x) {
        return y;
    }
    return x;
}

int minimumCost(int* nums, int numsSize) {
    int sz = numsSize;
    int min_n = 51 * 3;
    for (int j = 1; j < sz; j++) {
        for (int k = j + 1; k < sz; k++) {
            min_n = min2(min_n, nums[0] + nums[j] + nums[k]);
        }
    }
    return min_n;
}
