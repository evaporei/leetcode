int majorityElement(int *nums, int numsSize){
  int maj = 0,
      count = 0;

  for (int i = 0; i < numsSize; i++) {
    if (count == 0)
      maj = nums[i];
    count += maj == nums[i] ? 1 : -1;
  }

  return maj;
}
