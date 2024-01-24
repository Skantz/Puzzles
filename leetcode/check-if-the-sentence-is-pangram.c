#include <stdbool.h>

bool checkIfPangram(char* sentence) {
    bool b[27] = { false };

    for (int i = 0; i < 26; i++) {
        b[i] = false;
    }

    int start = (int) 'a';
    while (*sentence != '\0') {
        int c = ((int) *sentence) - start;
        if ((c >= 0) && (c < 27)) {
            b[c] = true;
        }
        sentence++;
    }
    int i = 0;
    while (i < 26) {

        if (!b[i]) {
            return 0;
        }
        i++;
    }
    return true;
}
