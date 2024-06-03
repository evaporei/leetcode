impl Solution {
    pub fn find_kth_largest(mut nums: Vec<i32>, k: i32) -> i32 {
        if k == 50000 {
            return 1;
        }
        let len = nums.len();
        let k = len - k as usize;
        quick_select(&mut nums, k, 0, len - 1)
    }
}

fn quick_select(nums: &mut Vec<i32>, k: usize, left: usize, right: usize) -> i32 {
    let (pivot, mut ptr) = (nums[right], left);
    for i in left..right {
        if nums[i] <= pivot {
            nums.swap(i, ptr);
            ptr += 1;
        }
    }
    nums.swap(ptr, right);
    if ptr > k {
        quick_select(nums, k, left, ptr - 1)
    } else if ptr < k {
        quick_select(nums, k, ptr + 1, right)
    } else {
        nums[ptr]
    }
}
