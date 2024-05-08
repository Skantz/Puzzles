int balancedStringSplit(char* s) {
    int r = 0;
    int z = 0;
    while (*s != '\0') {
        if (*s == 'L') {
            z += 1;
        } else {
            z -= 1;
        }
        if (z == 0) {
            r++;
        }
        s++;
    }
    return r;
}
