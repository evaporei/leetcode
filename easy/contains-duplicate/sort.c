#include <stdlib.h>

int compare_ints(const void *a, const void *b) {
    int x = *(int*) a;
    int y = *(int*) b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;

    // return x - y; // with non leetcode values, could have issue with overflow
}

bool containsDuplicate(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(int), compare_ints);
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] == nums[i+1])
            return true;
    }
    return false;
}
