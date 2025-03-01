typedef struct Pair {
    int idx;
    int value;
} Pair;

int compare_pairs(const void *a, const void *b) {
    Pair *p1 = (Pair*) a;
    Pair *p2 = (Pair*) b;
    int x = p1->value;
    int y = p2->value;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;

    // return x - y; // with non leetcode values, could have issue with overflow
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    Pair *pairs = malloc(sizeof(Pair) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        pairs[i].idx = i;
        pairs[i].value = nums[i];
    }
    qsort(pairs, numsSize, sizeof(Pair), compare_pairs);

    int i = 0, j = numsSize - 1;
    while (i < j) {
        if (pairs[i].value + pairs[j].value > target)
            j -= 1;
        else if (pairs[i].value + pairs[j].value < target)
            i += 1;
        else {
            int *returnNums = malloc(sizeof(int) * 2);
            *returnSize = 2;

            returnNums[0] = pairs[i].idx;
            returnNums[1] = pairs[j].idx;
            return returnNums;
        }
    }

    return NULL;
}
