#include <stdbool.h>
#include <stdlib.h>

bool contains(int* lst, int size, int e) {
    int* c = lst;
    for (int i = 0; i < size; i++) {
        if (*c == e) {
            return true;
        }
        c++;
    }
    return false;
}

int* intersection(int* nums1, int sz1, int* nums2, int sz2, int* retsz) {
    *retsz = 0;
    int* arr = (int*) malloc((sz1 + sz2) * sizeof(int));
    int* ret = arr;
    int* iter = nums1;
    int* target = nums2;
    int end = sz1;
    int targetsz = sz2;
    if (sz1 < sz2) {
        iter = nums2;
        target = nums1;
        end = sz2;
        targetsz = sz1;
    }
    for (int i = 0; i < end; i++) {
        if (contains(target, targetsz, *iter) && (!contains(ret, *retsz, *iter))) {
            *arr = *iter;
            arr++;
            (*retsz)++;
        }
        iter++;
    }
    return ret;
}
