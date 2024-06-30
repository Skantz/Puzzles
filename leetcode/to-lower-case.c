char* toLowerCase(char* s) {
    if (!s) {
        return s;
    }
    char* save = s;
    while (*s != '\0') {
        if (*s >= 'A' && *s <= 'Z') {
            *s += 32;
        }
        s++;
    }
    return save;
}
