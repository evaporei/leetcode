class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 10000:
            nums.sort()
            return nums
        return quicksort(nums, 0, len(nums) - 1)

def partition(arr: List[int], left: int, right: int) -> int:
    # Randomly choose a pivot and swap with the first element
    pivot_index = random.randint(left, right)
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    pivot = arr[left]

    i, j = left + 1, right
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[left], arr[j] = arr[j], arr[left]
    return j

def quicksort(arr: List[int], left: int, right: int):
    if left < right:
        middle = partition(arr, left, right)
        quicksort(arr, left, middle-1)
        quicksort(arr, middle+1, right)
    return arr
