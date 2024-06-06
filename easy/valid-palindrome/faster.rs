impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s: Vec<char> = s.chars()
            .filter(|ch| char::is_alphanumeric(*ch))
            .map(|ch| ch.to_ascii_lowercase())
            .collect();
        let (mut low, mut high) = (0, s.len().checked_sub(1).unwrap_or(0));
        while low < high {
            if s[low] != s[high] {
                return false;
            }
            low += 1;
            high -= 1;
        }
        true
    }
}
