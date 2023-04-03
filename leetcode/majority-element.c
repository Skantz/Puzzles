int majorityElement(int* nums, int numsSize){
  int first = nums[0];
  int second;
  int cnt_a = 1;
  int cnt_b = 0;
  for (int i = 1; i < numsSize; i++) {
    if (nums[i] == first)
      cnt_a++;
    else {
      second = nums[i];
      cnt_b++; }
  }
  if (cnt_a >= cnt_b)
    return first;
  return second;
}
