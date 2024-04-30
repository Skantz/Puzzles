int max2(int x, int y) {
    if (x < y) {
        return y;
    }
    return x;
}

int addedInteger(int* nums1, int sz1, int* nums2, int sz2) {
    int maxx1 = 0;
    int maxx2 = 0;
    for (int i = 0; i < sz1 && i < sz2; i++) {
        maxx1 = max2(maxx1, *(nums1++));
        maxx2 = max2(maxx2, *(nums2++));
    }
    return maxx2 - maxx1;
}
