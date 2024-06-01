int isArraySpecial(int* nums, int nz) {
  if (nz < 2) {
    return 1;
  }
  for (int i = 1; i < nz; i++) {
    if ((1 & nums[i]) == (1 & nums[i - 1])) {
        return 0;
    }
  }
  return 1;
}
