double average(int* salary, int salarySize) {
    int sz = salarySize;
    int s = 0;
    int min_ = 1000000;
    int max_ = 1000;
    for (int i = 0; i < sz; i++) {
        int el = salary[i];
        s += el;
        if (el < min_) {
            min_ = el;
        }
        if (max_ < el) {
            max_ = el;
        }
    }
    s -= max_;
    s -= min_;
    return (double)s / (sz - 2);
}
