#include <stdbool.h>

bool isIsomorphic(unsigned char* s, unsigned char* t) {

    unsigned char convert1[256];
    unsigned char convert2[256];
    for (int i = 0; i < 256; i++){
        convert1[i] = 0;
        convert2[i] = 0;
    }

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
