int arraySign(int* nums, int numsSize) {
    int ns = numsSize;
    int sign = 1;
    for (int i = 0; i < ns; i++) {
        if (nums[i] == 0) {
            return 0;
        }
        if (nums[i] < 0) {
            sign *= (-1);
        }
    }
    return sign;
}
