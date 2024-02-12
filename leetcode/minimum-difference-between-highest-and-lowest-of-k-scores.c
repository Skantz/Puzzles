#include <limits.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
  const int* ca = a;
  const int* cb = b;
  return (*ca > *cb) - (*ca < *cb);
}

int minimumDifference(int* nums, int numsSize, int k) {
    int nz = numsSize;
    // sort
    qsort(nums, nz, sizeof(int), compare);
    // window
    int ret = INT_MAX;
    for (int i = 0; i < nz - k + 1; i++) {
        int maxx = INT_MIN;
        int minn = INT_MAX;
        for (int j = 0; j < k; j++) {
            if (maxx < nums[i + j]) {
                maxx = nums[i + j];
            }
            if (nums[i + j] < minn) {
                minn = nums[i + j];
            }
        }
        if ((maxx - minn) < ret) {
            ret = maxx - minn;
        }
    }
    return ret;
}
