int search(int* nums, int numsSize, int target){
    return bs(nums, 0, numsSize, target);
}

int bs(int *arr, int low, int high, int target) {
    if (low > high)
        return -1;

    int mid = (low + high) / 2;

    if (arr[mid] == target)
        return mid;
    else if (arr[mid] > target)
        return bs(arr, low, mid - 1, target);
    else // if (arr[mid] < target)
        return bs(arr, mid + 1, high, target);
}
