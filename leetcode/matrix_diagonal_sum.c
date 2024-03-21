int diagonalSum(int** mat, int r_n, void* _) {
    (void)_;
    int s = 0;
    for (int i = 0; i < r_n; i++) {
        int* r = *mat;
        int p1 = r[i];
        int p2 = r[r_n - 1 - i];
        s += (p1 + p2);
        if (i == (r_n - 1 - i)) {
            s -= p2;
        }
        mat++;
    }
    return s;
}
