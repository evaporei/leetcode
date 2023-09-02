#![allow(unused)]

#[inline(always)]
fn is_even(n: usize) -> bool {
    n % 2 == 0
}

#[inline(always)]
/// Contraints:
/// 1 >= s.len() <= 10^4 (10_000, 10k)
/// s = { "(" | ")" | "[" | "]" | "{" | "}" }
fn is_valid(s: &str) -> bool {
    if !is_even(s.len()) || matches!(s.chars().next(), Some(')') | Some(']') | Some('}')) {
        return false;
    }

    let mut stack = Vec::with_capacity(s.len() / 2);

    for c in s.chars() {
        match c {
            '(' | '[' | '{' => stack.push(c),
            ')' => match stack.pop() {
                Some('(') => continue,
                Some(_) | None => return false,
            },
            ']' => match stack.pop() {
                Some('[') => continue,
                Some(_) | None => return false,
            },
            '}' => match stack.pop() {
                Some('{') => continue,
                Some(_) | None => return false,
            },
            _ => panic!(""),
        };
    }

    stack.len() == 0
}

#[test]
fn test_is_valid_open_close_one_paren() {
    assert_eq!(is_valid("()"), true);
}

#[test]
fn test_is_valid_all_open_close() {
    assert_eq!(is_valid("()[]{}"), true);
}

#[test]
fn test_is_valid_half_paren_bracket() {
    assert_eq!(is_valid("(]"), false);
}

#[test]
fn test_is_valid_mixture() {
    assert_eq!(is_valid("([)]"), false);
}

#[test]
fn test_is_valid_complex() {
    assert_eq!(
        is_valid("([{}{}()][]()()[([])])[{{()}}([])]{({{}{}}())}"),
        true
    );
}
