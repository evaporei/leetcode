impl Solution {
    pub fn max_area_of_island(mut grid: Vec<Vec<i32>>) -> i32 {
        let (rows, cols) = (grid.len(), grid[0].len());

        let mut max_area = 0;
        for i in 0..rows {
            for j in 0..cols {
                max_area = std::cmp::max(max_area, dfs(&mut grid, i, j));
            }
        }
        max_area
    }
}

fn dfs(grid: &mut Vec<Vec<i32>>, i: usize, j: usize) -> i32 {
    let (rows, cols) = (grid.len(), grid[0].len());

    if i >= rows || j >= cols || grid[i][j] != 1 {
        return 0
    }
    grid[i][j] = -1;
    
    1 + dfs(grid, i - 1, j) +
        dfs(grid, i + 1, j) +
        dfs(grid, i, j - 1) +
        dfs(grid, i, j + 1)
}
