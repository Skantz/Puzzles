int minOperations(int* nums, int nsz, int k) {
    int s = 0;
    for (int i = 0; i < nsz; i++) {
        if (*nums++ < k) {
            s++;
        }
    }
    return s;
}
