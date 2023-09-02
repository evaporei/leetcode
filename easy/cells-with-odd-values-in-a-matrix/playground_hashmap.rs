#![allow(unused)]

use std::collections::HashMap;

#[inline(always)]
/// Constraints:
///
/// 1 <= m, n <= 50
/// 1 <= indices.length <= 100
/// 0 <= r < m
/// 0 <= c < n
fn odd_cells(m: i32, n: i32, indices: Vec<Vec<i32>>) -> i32 {
    let mut matrix: HashMap<(i32, i32), bool> = HashMap::new();
    for idx in indices {
        let r = idx[0];
        let c = idx[1];

        {
            for i in 0..n {
                let is_odd = matrix.entry((r, i)).or_default();
                *is_odd = !*is_odd;
            }
        }

        {
            for i in 0..m {
                let column_item = matrix.entry((i, c)).or_default();
                *column_item = !*column_item;
            }
        }
    }

    let mut odd_count = 0;

    for i in 0..m {
        for j in 0..n {
            if let Some(true) = matrix.get(&(i, j)) {
                odd_count += 1;
            }
        }
    }

    odd_count
}

#[test]
fn test_m_2_n_3_idx_01_11() {
    assert_eq!(odd_cells(2, 3, vec![vec![0, 1], vec![1, 1]]), 6);
}

#[test]
fn test_m_2_n_2_idx_11_00() {
    assert_eq!(odd_cells(2, 2, vec![vec![1, 1], vec![0, 0]]), 0);
}

#[test]
fn test_m_48_n_37_idx_4005() {
    assert_eq!(odd_cells(48, 37, vec![vec![40, 5]]), 83);
}
