use std::collections::{HashSet, VecDeque};

impl Solution {
    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {
        if grid.is_empty() {
            return 0;
        }
        let mut count = 0;
        let (rows, cols) = (grid.len(), grid[0].len());

        for i in 0..rows {
            for j in 0..cols {
                if grid[i][j] == '1' {
                    count += 1;
                    dfs(&mut grid, i, j);
                }
            }
        }

        count
    }
}

fn dfs(grid: &mut Vec<Vec<char>>, i: usize, j: usize) {
    let (rows, cols) = (grid.len(), grid[0].len());

    if i < 0 || j < 0 || i >= rows || j >= cols {
        return;
    }
    if grid[i][j] != '1' {
        return;
    }
    if grid[i][j] == '1' {
        grid[i][j] = '#';
    }

    dfs(grid, i - 1, j);
    dfs(grid, i + 1, j);
    dfs(grid, i, j - 1);
    dfs(grid, i, j + 1);
}
