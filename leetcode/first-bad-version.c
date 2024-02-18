#include <stdbool.h>

bool isBadVersion(int);

int bin_search(bool (*arr)(int), unsigned int e, unsigned int l, unsigned int r) {
   if (r < l) {
     return -1;
   }
   unsigned int p = l + ((r - l) / 2);
   if ((*arr)(p) == e && ((p == 0) || (*arr)(p - 1) != e)) {
     return p;
   }
   if ((*arr)(p) < e) {
     return bin_search(arr, e, p + 1, r);
   }
   return bin_search(arr, e, l, p - 1);
}

int firstBadVersion(unsigned int n) {
    int s = bin_search(&isBadVersion, 1, 0, n - 1);
    if (-1 < s) {
        return s;
    }
    return n;
}
