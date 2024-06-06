impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let inversed: String = s.chars().filter(|ch| char::is_alphanumeric(*ch)).map(|ch| ch.to_ascii_lowercase()).rev().collect();

        for (ch, rev_ch) in s.chars().filter(|ch| char::is_alphanumeric(*ch)).map(|ch| ch.to_ascii_lowercase()).zip(inversed.chars()) {
            if ch != rev_ch {
                return false;
            }
        }

        true
    }
}
