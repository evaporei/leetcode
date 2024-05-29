impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut max = 0;
        let mut left = 0;
        let mut right = height.len() - 1;
        while left < right {
            max = std::cmp::max(max, area(&height, left, right));
            if height[left] > height[right] {
                right -= 1;
            } else {
                left += 1
            }
        }
        max
    }
}

#[inline(always)]
fn area(height: &Vec<i32>, i: usize, j: usize) -> i32 {
    let min = std::cmp::min(height[i], height[j]);
    min * (j as i32 - i as i32)
}
