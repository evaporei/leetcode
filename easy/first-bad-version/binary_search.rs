// The API isBadVersion is defined for you.
// isBadVersion(version:i32)-> bool;
// to call it use self.isBadVersion(version)

impl Solution {
    pub fn first_bad_version(&self, n: i32) -> i32 {
        let mut low = 1;
        let mut high = n;
        let mut min_bad_version = n;

        while low <= high {
            let mid = low + (high - low) / 2;

            if self.isBadVersion(mid) {
                min_bad_version = mid;

                // look backward
                high = mid - 1;
            } else {
                // look forward
                low = mid + 1;
            }
        }

        min_bad_version
    }
}
