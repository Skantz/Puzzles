#include <stdbool.h>

bool isOneBitCharacter(int* b, int sz) {
    int i = 0;
    while (i < sz - 1) {
        if (b[i]) {
            i++;
        }
        i++;
    }
    return (sz > i);
}
