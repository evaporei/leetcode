use std::iter::Peekable;
use std::vec::IntoIter;

enum Token {
    Number(i32),
    Plus,
    Minus,
    LParen,
    RParen,
}

enum Ast {
    Number(i32),
    Add(Box<Ast>, Box<Ast>),
    Sub(Box<Ast>, Box<Ast>),
    Neg(Box<Ast>),
}

fn tokenize(s: String) -> Vec<Token> {
    let mut chars = s.chars().peekable();
    let mut tokens = vec![];
    while let Some(ch) = chars.next() {
        let token = match ch {
            ' ' => continue,
            '(' => Token::LParen,
            ')' => Token::RParen,
            '+' => Token::Plus,
            '-' => Token::Minus,
            '0'..='9' => {
                let mut digits = String::new();
                digits.push(ch);
                while let Some(next_ch) = chars.peek() {
                    if !next_ch.is_ascii_digit() {
                        break;
                    }
                    digits.push(chars.next().unwrap());
                }
                Token::Number(digits.parse().unwrap())
            },
            _ => unreachable!(),
        };
        tokens.push(token);
    }
    tokens
}

fn parse(tokens: Vec<Token>) -> Ast {
    let mut tokens = tokens.into_iter().peekable();
    parse_expr(&mut tokens)
}

fn parse_expr(tokens: &mut Peekable<IntoIter<Token>>) -> Ast {
    let mut lhs = parse_term(tokens);
    while let Some(Token::Plus) | Some(Token::Minus) = tokens.peek() {
        let op = tokens.next().unwrap();
        let rhs = parse_term(tokens);
        match op {
            Token::Plus => lhs = Ast::Add(Box::new(lhs), Box::new(rhs)),
            Token::Minus => lhs = Ast::Sub(Box::new(lhs), Box::new(rhs)),
            _ => unreachable!("invalid token"),
        }
    }
    lhs
}

fn parse_term(tokens: &mut Peekable<IntoIter<Token>>) -> Ast {
    match tokens.next() {
        Some(Token::Number(n)) => Ast::Number(n),
        Some(Token::LParen) => {
            let expr = parse_expr(tokens);
            match tokens.next() {
                Some(Token::RParen) => {},
                _ => unreachable!("expected right paren"),
            }
            expr
        }
        Some(Token::Minus) => {
            let expr = parse_term(tokens);
            Ast::Neg(Box::new(expr))
        }
        _ => unreachable!("invalid token"),
    }
}

fn eval(ast: Ast) -> i32 {
    match ast {
        Ast::Number(n) => n,
        Ast::Add(lhs, rhs) => eval(*lhs) + eval(*rhs),
        Ast::Sub(lhs, rhs) => eval(*lhs) - eval(*rhs),
        Ast::Neg(expr) => -eval(*expr),
    }
}

fn rewrite(ast: Ast) -> Ast {
    match ast {
        Ast::Number(n) => Ast::Number(n),
        Ast::Add(lhs, rhs) => {
            let lhs = rewrite(*lhs);
            let rhs = rewrite(*rhs);
            match (&lhs, &rhs) {
                (Ast::Number(0), _) => rhs,
                (_, Ast::Number(0)) => lhs,
                (Ast::Number(a), Ast::Number(b)) => Ast::Number(a + b),
                _ => Ast::Add(Box::new(lhs), Box::new(rhs)),
            }
        }
        Ast::Sub(lhs, rhs) => {
            let lhs = rewrite(*lhs);
            let rhs = rewrite(*rhs);
            match (&lhs, &rhs) {
                (Ast::Number(0), _) => rewrite(Ast::Neg(Box::new(rhs))),
                (_, Ast::Number(0)) => lhs,
                (Ast::Number(a), Ast::Number(b)) => Ast::Number(a - b),
                _ => Ast::Sub(Box::new(lhs), Box::new(rhs)),
            }
        }
        Ast::Neg(expr) => {
            let inner = rewrite(*expr);
            match inner {
                // remove Neg node
                Ast::Number(n) => Ast::Number(-n),
                // double negation
                Ast::Neg(inner2) => *inner2,
                // realloc
                _ => Ast::Neg(Box::new(inner))
            }
        }
    }
}

impl Solution {
    pub fn calculate(s: String) -> i32 {
        let tokens = tokenize(s);
        let ast = parse(tokens);
        let simplified = rewrite(ast);
        eval(simplified)
    }
}
