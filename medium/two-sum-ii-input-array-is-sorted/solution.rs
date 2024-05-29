impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut low = 0;
        let mut high = numbers.len() - 1;

        while low < high {
            let sum = numbers[low] + numbers[high];
            if sum == target {
                return vec![low as i32 + 1, high as i32 + 1];
            }
            if sum > target {
                high -= 1;
            } else {
                low += 1;
            }
        }

        vec![]
    }
}
