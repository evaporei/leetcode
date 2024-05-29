impl Solution {
    pub fn flood_fill(mut image: Vec<Vec<i32>>, sr: i32, sc: i32, color: i32) -> Vec<Vec<i32>> {
        let (rows, cols) = (image.len(), image[0].len());
        let original = image[sr as usize][sc as usize];

        if original == color {
            return image;
        }

        bfs(&mut image, sr, sc, original, color);

        image
    }
}

use std::collections::{HashSet, VecDeque};

fn bfs(image: &mut Vec<Vec<i32>>, i: i32, j: i32, original: i32, color: i32) {
    let (rows, cols) = (image.len(), image[0].len());
    let directions = [(-1, 0), (1, 0), (0, -1), (0, 1)];

    let mut queue = VecDeque::from([(i, j)]);
    let mut visited = HashSet::from([(i, j)]);
    image[i as usize][j as usize] = color;

    while let Some((r, c)) = queue.pop_front() {
        for (dr, dc) in directions.iter() {
            let (row, col) = (r + dr, c + dc);
            if 0 <= row && row < rows as i32 &&
                0 <= col && col < cols as i32 &&
                image[row as usize][col as usize] == original &&
                !visited.contains(&(row, col)) {
                visited.insert((row, col));
                queue.push_back((row, col));
                image[row as usize][col as usize] = color;
            }
        }
    }
}
