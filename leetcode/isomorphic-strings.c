#include <stdbool.h>

bool isIsomorphic(unsigned char* s, unsigned char* t) {

    unsigned char convert1[128];
    unsigned char convert2[128];

    while (*s != '\0') {
        unsigned char x = *s;
        unsigned char y = *t;
        if (convert1[y] != 0) {
            if (convert1[y] != x) {
                return false;
            }
        } else {
            convert1[y] = x;
        }
        if (convert2[x] != 0) {
            if (convert2[x] != y) {
                return false;
            }
        } else {
            convert2[x] = y;
        }
        s++;
        t++;
    }
    return true;
}
