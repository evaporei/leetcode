impl Solution {
    pub fn flood_fill(mut image: Vec<Vec<i32>>, sr: i32, sc: i32, color: i32) -> Vec<Vec<i32>> {
        let (rows, cols) = (image.len(), image[0].len());
        let (sr, sc) = (sr as usize, sc as usize);
        let original = image[sr][sc];

        if original == color {
            return image;
        }

        dfs(&mut image, sr, sc, original, color);

        image
    }
}

fn dfs(image: &mut Vec<Vec<i32>>, i: usize, j: usize, original: i32, color: i32) {
    let (rows, cols) = (image.len(), image[0].len());

    if i >= rows || j >= cols {
        return;
    }
    if image[i][j] != original {
        return;
    }
    image[i][j] = color;
    
    dfs(image, i - 1, j, original, color);
    dfs(image, i + 1, j, original, color);
    dfs(image, i, j - 1, original, color);
    dfs(image, i, j + 1, original, color);
}
