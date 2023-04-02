int* countBits(int n, int* returnSize){
  int *c = (int*)malloc((n + 1)*sizeof(int));
  for (int i = 0; i < n + 1; i++)
    {c[i] = __builtin_popcount(i); }
  *returnSize = n + 1;
  return c;
}
